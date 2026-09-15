# Substantiate, Don't Assume

*Why the Auditor's Opinion Matters More Than Ever in the Age of AI*

An open-access Quarto book by Michael Borck. Twelve chapters follow a fictional information-security readiness assessment from mandate to an evidence-backed opinion.

## Read and practise

The free edition is the focus: [read online](https://michael-borck.github.io/substantiate-dont-assume/). The fixed book-only case, **SDA-2026.1**, supplies all core inputs in print and electronic form. Its cutoff is 30 June 2026. The live Tessera site and AI prompts are optional, separately versioned practice.

- `index.qmd`: audience, prerequisites, route and limits.
- `chapters/`: twelve stable chapter filenames in two acts.
- `appendices/`: AI method, fixed evidence pack, answer checks/rubric, primary sources and interview practice.
- `resources/sda-2026-1/`: original synthetic leavers, retest, finding ledger and SHA-256 manifest.
- `scripts/check_manuscript.py`: source-only regression checks.
- `EDITORIAL-REVISION.md`: changes, validation and outstanding release gates.

## Local build and checks

From the parent books workspace, with the publisher dependencies and Quarto/LaTeX installed:

```sh
python substantiate-dont-assume/scripts/check_manuscript.py
python book-publisher/publish.py --book sda --preprocess
python book-publisher/publish.py --book sda --llm
python book-publisher/publish.py --book sda --render
python book-publisher/tools/check_rendered_book.py substantiate-dont-assume
python book-publisher/publish.py --book sda --audit
```

HTML renders from this source. The publisher creates `_print_source/` and separate PDF/EPUB profiles, then copies canonical `substantiate-dont-assume.pdf` and `.epub` downloads into `_book/`. EPUB includes `copyright.qmd`; PDF uses the TeX rights page. A plain root `quarto render` is not the KDP preprocessing workflow.

These commands do not deploy, update the hosted chatbot, commit or upload to KDP. Do not use `--all` for local validation: it includes external publishing steps. Regenerate local chatbot/RAG inputs separately if desired, and refresh the hosted service only with release approval.

## Editorial and release boundaries

The approved revision preserves chapter order, supplies a standalone case, repairs the evidence-to-opinion chain, updates consequential explanations and retains only three extended AI endings. Standards target ISO/IEC 27001:2022 with Amd 1:2024 and NIST CSF 2.0; guidance editions are recorded in the source appendix.

Licence: **CC BY 4.0 International**, confirmed by the author. Existing artwork is unchanged. The author approved recasting unattributed audit anecdotes as fictional teaching examples. Verify separate artwork and Tessera-brand permissions, exact normative claims against authorised standards, a fresh-reader attempt and human release proof before publication.

KDP status remains **not yet published**, with no assigned ISBN in the publisher registry. Source revision, website deployment, chatbot refresh and KDP release are separate actions.

## Licence

Book content is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0 International)](https://creativecommons.org/licenses/by/4.0/). Original code examples and accompanying software are licensed under the [MIT License](https://opensource.org/licenses/MIT).

These grants cover material the author has authority to license. Separately credited third-party material retains its stated terms. Give appropriate credit, link the content licence and indicate changes; retain the MIT notice when reusing code.

See [LICENSE](LICENSE), [LICENSE-CONTENT.md](LICENSE-CONTENT.md) and [LICENSE-CODE.md](LICENSE-CODE.md) for scope and full terms.
