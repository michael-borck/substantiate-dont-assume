# Substantiate, Don't Assume

*Why the Auditor's Opinion Matters More Than Ever in the Age of AI*

An open-access Quarto book by **Michael Borck** on the discipline of information security auditing against international standards, with a clear stance on where the human auditor fits once machines can draft the work.

The book follows one engagement told twelve ways. You audit **Tessera**, a fast-growing B2B SaaS company chasing ISO/IEC 27001 certification, from the opening *Why?* through to the final *Conclude?*. Each chapter is one phase of a real certification-readiness engagement, built around the spine of the book: *substantiate, don't assume*.

---

## What lives here

- **`index.qmd`** — the Introduction (premise, AI stance, how the book works, conventions).
- **`chapters/`** — the twelve chapters (`01-why.qmd` … `12-conclude.qmd`), in two acts: **Engage** (build the case) and **Prove** (from suspicion to proof).
- **`appendices/`** — the drafter-to-evaluator loop reference.
- **`acknowledgments.qmd`, `about-author.qmd`, `copyright.qmd`** — front and back matter.
- **`CHAPTER_OUTLINE.md`** — the full blueprint: premise, AI stance, design principles, recurring features, the 12-chapter outline, and build/deployment notes. **Read this first.**
- **`_quarto.yml`, `styles.css`, `*.tex`, `*.yml`** — Quarto configuration, styling, and PDF/LaTeX support.

---

## Book at a glance

- **Premise:** AI is commoditising the technical craft of auditing (enumerate controls, sample, draft procedures). The auditor's moat is the **variation** AI cannot supply — judgement, professional scepticism, a defensible point of view. The job shifts from *drafter* to *expert evaluator*. Augmentation, not automation; efficiency is never worth sacrificing the critical thinking the profession depends on.
- **Spine:** professional scepticism — *substantiate, don't assume.*
- **Structure:** 12 chapters, one per question (`Why? → Risk? → … → Conclude?`), in two acts — **Engage** (build the case) and **Prove** (from suspicion to proof).
- **Recurring features (every chapter):** *AI Field Note* (use AI as a thinking partner), *Auditing AI* (audit *of* AI systems, where relevant), *Tessera Case*, *Evidence Locker prompt*.
- **Companion text:** *Conversation, Not Delegation* (https://michael-borck.github.io/conversation-not-delegation/) — the *how-to-use-AI-well* companion to this book's *what-we-verify* discipline.
- **Companion site:** **tessera.locoensayo.org** — a live, simulated company to audit, open all hours, no password.

---

## Build and deploy

- **Format:** Quarto book; renders to HTML + PDF + EPUB.
- **Build:** `quarto render` (or `quarto preview` for live drafting).
- **Hosting:** GitHub Pages, repo slug `substantiate-dont-assume`, served at `michaelborck.github.io/substantiate-dont-assume/`.
- **Licence:** Creative Commons BY (open access, attribution).
- **Standards:** the book targets ISO/IEC 27001:2022 and NIST CSF 2.0 from the outset; standards drift is handled by edition, not errata.

---

## Status

- [x] Title, premise, and AI stance confirmed
- [x] 12-chapter outline locked
- [x] Quarto project scaffolded (HTML + EPUB + PDF all render)
- [x] All twelve chapters drafted
- [ ] Final edit pass and deployment

---

## Decisions locked

- Title: *Substantiate, Don't Assume: Why the Auditor's Opinion Matters More Than Ever in the Age of AI*.
- Premise / AI stance: commoditisation → variation is the moat → evaluator not drafter.
- Spine: professional scepticism (*substantiate, don't assume*), stated in the Introduction and enacted in every chapter.
- *Conversation, Not Delegation* as the AI-craft companion.
- ISO/IEC 27001:**2022** as the control standard (not 2013).
- Chapter opener: epigraph + a 2–4 sentence Tessera field-report vignette (deliberately *not* comic panels — this book's professional tone calls for a credible, narrative opener).
- Callout system: blue *AI Field Note*, red *Auditing AI*, green *Evidence Locker*, slate *Tessera Case* box, plus generic yellow *Watch out* callouts.
- Companion site = **Tessera** at **tessera.locoensayo.org** (a *LocoEnsayo* rehearsal environment): kept full (all documents and staff, not stripped down), with red-herring distractors added; open all hours, no password.

---

*House style: no em dashes. Use periods, colons, semicolons, parentheses, or commas instead. En dashes for number ranges (2022–2026) are fine. Apply throughout when drafting and editing.*
