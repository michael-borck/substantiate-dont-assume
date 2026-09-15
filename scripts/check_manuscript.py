"""Source-only regression checks for the fixed SDA teaching engagement.

Run with Python 3; no generated book, network, model or third-party package needed.
These checks do not establish legal accuracy or replace reader/expert review.
"""

import csv
import hashlib
import json
import math
from pathlib import Path
import re
import unittest
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "resources" / "sda-2026-1"


def read(relative):
    return (ROOT / relative).read_text(encoding="utf-8")


def rows(name):
    with (DATA / name).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def elapsed(start, end):
    return (datetime.fromisoformat(end) - datetime.fromisoformat(start)).total_seconds() / 3600


def result(row, limit):
    if not row["identity_revoked"] or not row["key_revoked"]:
        return "insufficient evidence"
    delay = max(elapsed(row["terminated"], row[field]) for field in ("identity_revoked", "key_revoked"))
    return "exception" if delay > limit else "met"


class ManuscriptChecks(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ledger = json.loads((DATA / "ledger.json").read_text())
        cls.pack = read("appendices/b-case-pack.qmd")
        cls.conclusion = read("chapters/12-conclude.qmd")

    def test_complete_historical_population(self):
        records = rows("leavers.csv")
        self.assertEqual({r["id"] for r in records}, {f"L{i:03}" for i in range(1, 49)})
        self.assertEqual(len(records), 48)
        period = self.ledger["historical_period"]
        for row in records:
            self.assertLessEqual(period["start"], row["terminated"][:10])
            self.assertLessEqual(row["terminated"][:10], period["end"])
            for field in ("identity_revoked", "key_revoked"):
                self.assertGreaterEqual(elapsed(row["terminated"], row[field]), 0)
                self.assertEqual(datetime.fromisoformat(row[field]).utcoffset().total_seconds(), 8 * 3600)

    def test_both_policy_results_and_boundary(self):
        records = rows("leavers.csv")
        expected = {24: {"L007", "L019", "L031"}, 2: {"L007", "L019", "L031", "L044"}}
        self.assertEqual(self.ledger["historical_threshold_hours"], {"P-IT": 24, "P-HR": 2})
        for limit, ids in expected.items():
            self.assertEqual({r["id"] for r in records if result(r, limit) == "exception"}, ids)
        self.assertEqual(3 / len(records) * 100, 6.25)
        self.assertAlmostEqual(4 / len(records) * 100, 8.333333333)
        boundary = dict(records[0], key_revoked="2025-06-01T18:00+08:00")
        self.assertEqual(result(boundary, 2), "met")
        boundary["key_revoked"] = ""
        self.assertEqual(result(boundary, 2), "insufficient evidence")

    def test_printed_population_matches_csv(self):
        for row in rows("leavers.csv"):
            self.assertEqual(row["terminated"][11:16], "16:00")
            self.assertEqual(elapsed(row["terminated"], row["identity_revoked"]), 1)
            expected = f'| {row["id"]} | {row["terminated"][:10]} | {row["key_revoked"][:10]} | {row["key_revoked"][11:16]} |'
            self.assertEqual(self.pack.count(expected), 1)
        self.assertIn("Every last working day ends at **16:00**", self.pack)
        self.assertIn("17:00 on that day", self.pack)

    def test_exception_calculations(self):
        records = {r["id"]: r for r in rows("leavers.csv")}
        for identifier, hours in {"L007": 1128, "L019": 50, "L031": 72, "L044": 6}.items():
            row = records[identifier]
            self.assertEqual(elapsed(row["terminated"], row["key_revoked"]), hours)

    def test_sampling_is_separate_from_census(self):
        n = math.ceil(math.log(0.05) / math.log(0.95))
        self.assertEqual(n, 59)
        self.assertLessEqual(0.95 ** n, 0.05)
        self.assertGreater(0.95 ** (n - 1), 0.05)
        self.assertAlmostEqual((1 - 0.05 ** (1 / n)) * 100, 4.95, places=2)
        chapter = read("chapters/07-prove.qmd")
        self.assertIn("48 of 48: a census", chapter)
        self.assertIn("finite-population", chapter)
        self.assertNotIn("Hash (prefix)", chapter)

    def test_retest_cannot_close_f01(self):
        records = rows("retest.csv")
        self.assertEqual([r["id"] for r in records], [f"R{i:02}" for i in range(1, 7)])
        results = [result(r, self.ledger["prospective_threshold_hours"]) for r in records]
        self.assertEqual(results.count("met"), 5)
        self.assertEqual(results.count("insufficient evidence"), 1)
        self.assertEqual(results.count("exception"), 0)
        for row in records:
            self.assertGreater(row["terminated"][:10], self.ledger["workflow_effective"])
            self.assertLess(row["terminated"][:10], self.ledger["retest_reviewed"])
            day = int(row["terminated"][8:10])
            disabled = f"{day} June 17:00" if row["key_revoked"] else "No event supplied"
            self.assertIn(f'| {row["id"]} | {day} June 16:00 | {disabled} |', self.pack)
        finding = next(f for f in self.ledger["findings"] if f["id"] == "F01")
        self.assertEqual((finding["status"], finding["retest"]), ("open", "incomplete"))
        self.assertIn("R06 remains insufficiently evidenced", self.conclusion)

    def test_recovery_arithmetic_and_limits(self):
        recovery = self.ledger["recovery"]
        self.assertEqual(elapsed(recovery["loss"], recovery["service_checked"]) * 60, 330)
        self.assertEqual(elapsed(recovery["recovery_point"], recovery["loss"]) * 60, 40)
        self.assertEqual((recovery["rto_minutes"], recovery["rpo_minutes"]), (240, 15))
        self.assertTrue(recovery["integrity_passed"])
        self.assertFalse(recovery["production_cutover_verified"])
        self.assertFalse(recovery["key_dependency_verified"])
        self.assertAlmostEqual(30 * 24 * 60 * 0.001, 43.2)

    def test_all_findings_reach_the_opinion(self):
        findings = self.ledger["findings"]
        self.assertEqual({f["id"] for f in findings}, {f"F{i:02}" for i in range(1, 6)})
        report = read("chapters/11-report.qmd")
        for finding in findings:
            self.assertIn(finding["id"], report)
            self.assertIn(finding["id"] + ":", self.conclusion)
            self.assertTrue(finding["closure_requires"])
            for evidence in finding["evidence"]:
                self.assertRegex(self.pack, rf"## {evidence}:")
        critical = {f["id"] for f in findings if f["original_severity"] == "high" and f["status"] == "open"}
        self.assertEqual(critical, set(self.ledger["conclusion"]["critical_open_findings"]))
        self.assertEqual(self.ledger["conclusion"]["stage_2"], "defer")
        self.assertIn("does not establish whole-ISMS Stage 1 readiness", self.conclusion)
        self.assertIn("P01:", self.conclusion)

    def test_privacy_and_review_issues_survive_compression(self):
        for term in ("Notice/register", "terms and regions", "training-setting", "retention/deletion", "vendor incident", "monthly privileged", "quarterly ordinary"):
            self.assertIn(term.lower(), self.conclusion.lower())
        self.assertIn("30 calendar days", read("chapters/09-protect.qmd"))
        self.assertIn("directly related for sensitive information", read("chapters/09-protect.qmd"))

    def test_solo_route_and_three_optional_ai_endings(self):
        chapters = sorted((ROOT / "chapters").glob("[0-9][0-9]-*.qmd"))
        self.assertEqual(len(chapters), 12)
        self.assertEqual(sum(read(str(p.relative_to(ROOT))).count("## Take it to the AI") for p in chapters), 3)
        for index, chapter in enumerate(chapters, 1):
            text = chapter.read_text()
            self.assertIn(f"Engagement milestone {index}", text)
            self.assertIn("No AI", text)
            self.assertNotIn("—", text)
        self.assertIn("11/14", read("appendices/c-answer-checks.qmd"))
        self.assertIn("X01", self.pack)

    def test_configured_resources_and_licence(self):
        config = read("_quarto.yml")
        self.assertIn("- copyright.qmd", config)
        for name in ("b-case-pack", "c-answer-checks", "d-sources", "e-interview-guide"):
            self.assertIn(f"appendices/{name}.qmd", config)
        for ext in ("pdf", "epub"):
            self.assertIn(f"href: /substantiate-dont-assume.{ext}", config)
        for name in ("_quarto.yml", "copyright.qmd", "copyright-page.tex"):
            self.assertIn("4.0", read(name))
        self.assertIn("CC BY 4.0 International", config)
        for path in [ROOT / "index.qmd", *ROOT.glob("chapters/*.qmd"), *ROOT.glob("appendices/*.qmd")]:
            if path.name.startswith("._"):
                continue
            for target in re.findall(r"\]\(([^)]+\.qmd)(?:#[^)]+)?\)", path.read_text()):
                self.assertTrue((path.parent / target).is_file(), f"{path.name}: {target}")

    def test_pack_checksums(self):
        for line in (DATA / "SHA256SUMS").read_text().splitlines():
            digest, filename = line.split()
            self.assertEqual(hashlib.sha256((DATA / filename).read_bytes()).hexdigest(), digest, filename)


if __name__ == "__main__":
    unittest.main(verbosity=2)
