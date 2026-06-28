# Substantiate, Don't Assume — Book Project

**Status:** Spec & handoff for the ISYS6018 companion book.
**Location:** `/Volumes/Crucial X9/Projects/books/substantiate-dont-assume` — a peer of `conversation-not-delegation` in the `books/` workspace.
**Last updated:** 2026-06-28

This folder is the book's home in the `books/` workspace. It holds the planning/spec now; the Quarto book is scaffolded and drafted here, following the same structure as `conversation-not-delegation`.

---

## What lives here

- **`CHAPTER_OUTLINE.md`** — the full blueprint: premise, AI stance, design principles, recurring features, the 12-chapter outline, relationship to the course and to *Conversation, Not Delegation*, and build/deployment notes. **Read this first.**

---

## Book at a glance

- **Title:** *Substantiate, Don't Assume: Why the Auditor's Opinion Matters More Than Ever in the Age of AI*
- **Premise:** AI is commoditising the technical craft of auditing (enumerate controls, sample, draft procedures). The auditor's moat is the **variation** AI cannot supply — judgement, professional skepticism, a defensible point of view. The job shifts from *drafter* to *expert evaluator*. Augmentation, not automation; efficiency is never worth sacrificing the critical thinking the profession depends on.
- **Spine:** professional skepticism — *substantiate, don't assume.*
- **Structure:** 12 chapters, one per weekly question, mirroring the ISYS6018 twelve-week arc (`Why? → Risk? → … → Conclude?`), in two acts — **Engage** (build the case) and **Prove** (from suspicion to proof).
- **Recurring features (every chapter):** *AI Field Note* (use AI as a thinking partner), *Auditing AI* (audit *of* AI systems, where relevant), *Tessera Case*, *Evidence Locker prompt*.
- **Companion text:** *Conversation, Not Delegation* (https://michael-borck.github.io/conversation-not-delegation/) — the *how-to-use-AI-well* companion to this book's *what-we-verify* discipline.

---

## Where this project lives

- **Project home:** `/Volumes/Crucial X9/Projects/books/substantiate-dont-assume` — alongside `conversation-not-delegation` and the other Quarto book projects.
- **Structural template:** `../conversation-not-delegation/` — a concepts book (not a Python-series book), the closest analog. Scaffold this book to match: `_quarto.yml`, `index.qmd`, `chapters/`, `appendices/`, `cover.png`, `styles.css`.
- **Target deployment:** Quarto book → GitHub Pages. Repo slug `substantiate-dont-assume` → `michael-borck.github.io/substantiate-dont-assume/`. Licence: CC BY.
- **Publishing tooling:** the `books/` workspace ships a `../book-publisher/` (`publish.py`, `books.yml`) used by the other books.

---

## Relationship to ISYS6018

- **Course repo:** `/Volumes/Crucial X9/Projects/curtin/units/isys6018-information-security-audit-and-control/`
- **Course outline:** `/Volumes/Crucial X9/Projects/curtin/units/isys6018-information-security-audit-and-control/ISYS6018_outline.md` — its *Companion Book & AI Stance* section links back to this project.
- **Lockstep rule:** the book and the course share the same twelve topics. **Chapter *N* = Topic *N*, delivered in Week *N* of the course.** A topic is one weekly question (*Why? → … → Conclude?*) plus its key concepts; the book delivers it as a chapter, the course delivers it as a week. The case company may differ between the two (the book's Tessera companion site versus Cloudcore in the course); the **topic** is what stays locked. If the course arc changes, the chapter list changes with it.
- Note: book and course now live in different project trees (`books/` vs `curtin/units/`); treat the absolute paths above as the source of truth for cross-references.

---

## Status

- [x] Title confirmed
- [x] Premise + AI stance written
- [x] 12-chapter outline co-designed with the twelve-week arc
- [x] Wired into the ISYS6018 outline
- [x] Relocated to the `books/` workspace and renamed to `substantiate-dont-assume`
- [x] Quarto project scaffolded here (mirrors `conversation-not-delegation`; HTML + EPUB + PDF all render)
- [x] Introduction + Chapter 1 drafted (vertical slice; callout system + 4 recurring features live)
- [ ] Remaining chapters drafted
- [ ] Book rendered and deployed

---

## How to resume (for the next session)

1. **Read `CHAPTER_OUTLINE.md`** — it is the blueprint; do not re-derive the structure.
2. **The Quarto book is scaffolded here** (`_quarto.yml`, `index.qmd`, `chapters/`, `appendices/`, and the support/LaTeX files), mirroring `../conversation-not-delegation/`. Drafting happens in this folder (the drafting-workflow question is resolved — see Open questions). The callout/engagement system is locked; see the Introduction's *Conventions used in this book*.
3. **The vertical slice is done** (Introduction + Chapter 1). Next: draft Chapters 2–12, one per topic. Each chapter opens with an **epigraph + a 2–4 sentence Tessera field-report vignette** and carries all four recurring features (🤖 AI Field Note, 🔍 Auditing AI, 🗂️ Tessera Case, 🗄️ Evidence Locker). Chapters can be drafted in parallel once the voice and format are approved.
4. **Keep the book in lockstep with the ISYS6018 outline** on the twelve topics (Chapter *N* = Topic *N*, delivered in Week *N*); the current arc lives at `/Volumes/Crucial X9/Projects/curtin/units/isys6018-information-security-audit-and-control/ISYS6018_outline.md`. The book uses Tessera; the course uses Cloudcore; the shared spine is the topic.
5. **Decisions already locked — do not relitigate:**
   - Title (above)
   - Premise / AI stance (commoditisation → variation is the moat → evaluator not drafter)
   - Professional-skepticism spine ("substantiate, don't assume")
   - Co-design with the twelve-week arc
   - *Conversation, Not Delegation* as the AI-craft companion
   - ISO/IEC 27001:**2022** as the control standard (not 2013)
   - Chapter opener = epigraph + Tessera field-report vignette (deliberately *not* comic panels — CND uses comics for its general audience; this book's professional tone calls for a credible, narrative opener)
   - Callout system: blue AI Field Note, red Auditing AI, green Evidence Locker, slate Tessera Case box, plus generic yellow Watch-out callouts
   - **House style: no em dashes.** Use periods, colons, semicolons, parentheses, or commas instead. En dashes for number ranges (2022–2026) are fine. Apply throughout when drafting and editing.
   - **Companion site = Tessera** at **tessera.locoensayo.org** (a *LocoEnsayo* rehearsal environment). Built by porting and retheming Cloudcore, but kept full (all documents and staff, not stripped down) with red-herring distractors added; open all hours, no password. The book's case company is Tessera; the course uses Cloudcore. Lockstep is on the topic, not the company.

---

## Open questions for the author

- Drafting workflow: ~~write prose directly in this folder, or via a separate tool?~~ **Resolved — draft prose directly in this folder** (the `substantiate-dont-assume/` Quarto project). The earlier "separate project" note in `CHAPTER_OUTLINE.md` §8 has been corrected.
- Preferred chapter length / total target word count?
- ~~Should the *Tessera Case* artefacts be shared verbatim with the course repo, or re-written for the book?~~ **Resolved** — the book gets its own simulation (Tessera), ported and rethemed from Cloudcore, kept full (all docs + staff) with red-herring distractors. No verbatim sharing with the course repo.
