# Substantiate, Don't Assume
## Why the Auditor's Opinion Matters More Than Ever in the Age of AI

**Author:** Michael Borck
**Status:** Chapter outline / blueprint for the book
**Format:** Open-access Quarto book, deployed to GitHub Pages (mirroring `michael-borck.github.io/conversation-not-delegation/`)

---

## 1. Why this book

Information security auditing is standards-driven, not textbook-driven — and that is a weakness for the person trying to learn it. The discipline's core references are ISO/IEC 27001, NIST CSF, the Privacy Act: authoritative, but not a *narrative* a reader can follow end to end. There is no spine. *Substantiate, Don't Assume* is that spine: a readable, opinionated, open-access book that follows one engagement from start to finish.

The book solves a second, harder problem. The discipline needs to be **AI-aware** — not by bolting "use ChatGPT" onto each topic, but by giving the reader a coherent stance on what professional judgement is *worth* when machines can draft the technical work. The book is where that stance lives.

---

## 2. The premise: judgement in a commoditised world

The book takes a deliberately pragmatic position on AI — steering clear of both alarmism and techno-utopianism — and lands it on the auditor's desk.

**The commoditisation argument.** The technical craft of information security auditing — enumerating controls, mapping them to frameworks, sampling, drafting test procedures, writing up findings — is exactly the kind of work that generative AI is rapidly commoditising. An AI can list ISO 27001:2022's 93 controls faster and more completely than any junior auditor. If the only thing an auditor does is *produce* that list, the auditor has no edge.

**The variation argument (the human moat).** If an AI is equally good at running every company, then by definition there is no variation between companies that use it generically — and no variation means no competitive edge. The edge comes from variation: human agency, individual taste, a genuine point of view about what matters. For an auditor, that variation shows up as *professional scepticism* — the willingness to look at a polished policy and ask whether the evidence supports it, to decide which of a hundred small gaps actually matters, to form a defensible opinion rather than a confident average. The machine produces the draft; the auditor supplies the judgement. That judgement is the moat.

**From drafter to evaluator.** As AI shifts from chatbots to agentic systems capable of running procedures independently, the auditor's job changes: from creator of "shitty first drafts" to **expert evaluator and editor** of AI-generated work. This is the discipline the book teaches explicitly: every AI-drafted artefact is followed by the evaluator's correction, the judgement the machine could not supply.

**Augmentation, not automation.** The book's stance is proactive: use these tools for human augmentation and personalised learning — not passive automation that quietly atrophies the critical thinking the profession depends on. Efficiency is not the goal; *defensible judgement* is. If you use AI to skip the thinking, you have done the work wrong, no matter how good the output looks.

This premise is the thread that runs through every chapter.

---

## 3. Design principles

1. **One engagement, twelve phases.** Each chapter is one topic: a single question (`Why? → Risk? → … → Conclude?`) plus its key concepts. The twelve chapters follow the phases of a real certification-readiness engagement, in the order an auditor actually lives them.
2. **Professional scepticism as the spine.** *Substantiate, don't assume* is stated in the introduction and enacted in every chapter.
3. **One case company throughout the book.** A single case company runs through the book, so every concept lands on a concrete artefact. The case company is **Tessera**, hosted on the open companion site **tessera.locoensayo.org** under the *LocoEnsayo* rehearsal environments: kept full (all documents and staff), with red-herring distractors added; open all hours, no password.
4. **AI as a first-class topic, integrated not appended.** Every chapter carries two recurring features (below): one on *using* AI as a thinking partner, one on *auditing* AI where the topic demands it.

---

## 4. Recurring features

Every chapter includes:

- **AI Field Note**: how to use AI as a thinking partner for *this* chapter's task, with a worked example against Tessera. Demonstrates prompt refinement and, crucially, where the AI got it wrong and the auditor corrected it.
- **Auditing AI** *(where relevant)* — the chapter's concept applied *to* AI systems: which framework controls an AI deployment falls under, how you audit an AI-assisted control, what evidence an AI system produces.
- **Tessera Case** — a concrete artefact from the Tessera engagement that anchors the chapter.
- **Evidence Locker prompt** — the one artefact the reader should lock into their cumulative working-paper file that chapter. By the final chapter the locker *is* the audit.

---

## 5. Chapter outline

Two acts: **Engage** (build the case) and **Prove** (from suspicion to proof).

### Front matter

**Introduction — The Audit Mindset**
What information security auditing actually is; why "trust, but verify" is the profession's founding maxim; the professional-scepticism principle stated as *substantiate, don't assume*; and the book's AI stance (the premise above) laid out in full. The chapter that tells the reader why the rest of the book matters.

### Part I — Engage: build the case

**Chapter 1 — Why? The auditor's mandate and ethics**
The auditor's roles (counsellor, partner, investigator); independence and objectivity; the ISACA Code of Ethics; why an organisation would invite an audit. *AI Field Note:* using AI to explore control categories — and spotting when its examples are generic. *Auditing AI:* can an AI be "independent"?

**Chapter 2 — Risk? Foundations of risk management**
The risk lifecycle; likelihood × impact; the risk register; treatment options (avoid / mitigate / transfer / accept); residual risk; ISO 27005 and NIST SP 800-30. *AI Field Note:* having AI draft a risk matrix — then editing the ratings with judgement it cannot supply. *Tessera Case:* the preliminary Tessera risk matrix.

**Chapter 3 — Which? Frameworks and standards**
ISO/IEC 27001:2022 (4 themes, 93 controls); NIST CSF 2.0 (including Govern); ASD Essential Eight; how to choose, map, and reconcile frameworks. *Auditing AI:* which controls apply to an AI deployment, and the new 2022 controls (cloud services, threat intelligence) that AI makes load-bearing.

**Chapter 4 — Scope? Audit planning and methodology**
Audit objectives, scope, materiality, criteria; the engagement letter; the audit programme; the six-stage audit lifecycle (ISO 19011). The chapter where readers learn *how* to audit before *what*. *AI Field Note:* using AI to draft an audit programme — and stress-testing its scope assumptions.

**Chapter 5 — Expect? Technical control objectives**
Access control (IAM, least privilege), network security, cryptography and key management, multi-tenant SaaS controls, the AWS shared-responsibility model. Framed as control *objectives* — what "good" looks like, the thing you test against. *Auditing AI:* securing and auditing the AI systems that now sit inside the technical estate.

**Chapter 6 — Assess? Physical, people, and ISMS controls**
Physical and environmental security; HR security across the employment lifecycle; asset management; supplier relationships; ISMS governance and documentation. Ends Act I: the preliminary readiness opinion formed from limited access. *AI Field Note:* the desk-audit limits of AI when you can only read documents.

### Part II — Prove: from suspicion to proof

**Chapter 7 — Prove? Evidence collection and testing**
Evidence types; sufficiency and appropriateness; statistical sampling; chain of custody; testing procedures; audit interviewing. *Auditing AI:* AI-generated evidence — can you trust a log an AI produced, and how do you test a control an AI runs?

**Chapter 8 — Comply? Policy evaluation**
Policy *effectiveness* versus mere compliance; ISO 27001 A.5 organizational controls; the gap between policy intent and operational reality. *AI Field Note:* AI as a policy-gap analyst — and its tendency to confabulate "compliance" where nuance is required.

**Chapter 9 — Protect? Data protection and privacy**
The Australian Privacy Principles; the Notifiable Data Breaches scheme; cross-border transfer and sovereignty; Privacy Impact Assessment; data masking and deletion. *Auditing AI:* the privacy risks of AI systems themselves — training data, model inversion, inference.

**Chapter 10 — Recover? Business continuity and incident management**
BCDR; RTO/RPO; testing methods; incident response auditing; ICT readiness for business continuity. *Tessera Case:* what happens to a multi-tenant SaaS when a region fails.

**Chapter 11 — Report? Findings and the audit opinion**
The 5C+R finding format (Criteria, Condition, Cause, Consequence, Corrective action + Recommendation); risk rating; root-cause analysis; executive reporting; forming a defensible audit opinion. The chapter where judgement is most visible — and where the evaluator-not-drafter thesis lands hardest. *AI Field Note:* AI drafts the finding; the auditor supplies the opinion.

**Chapter 12 — Conclude? Certification, defence, and the future of audit**
The certification-readiness opinion; defending it under board questioning; cloud and third-party (SOC report) assurance; and the future — **AI in audit** and **auditing AI** as the two faces of the next decade. Closes the book by returning to the premise: in a world where the technical work is commoditised, the defensible human opinion is the whole point.

---

## 6. Relationship to *Conversation, Not Delegation*

*Conversation, Not Delegation* is the companion on the AI dimension. Where *Substantiate, Don't Assume* teaches the audit discipline (the *what we verify*), *Conversation, Not Delegation* (https://michael-borck.github.io/conversation-not-delegation/) teaches the *how-to-use-AI-well* craft (the trust tool, staying in the loop, compensating for AI's predictable weaknesses). The two are complementary: one is the *what we verify*, the other the *how we work with the machine*.

---

## 7. Build and deployment

- **Format:** Quarto book (`quarto create-project --type book`), Markdown sources, renders to HTML + PDF + EPUB.
- **Hosting:** GitHub Pages, repo slug `substantiate-dont-assume`, served at `michael-borck.github.io/substantiate-dont-assume/`.
- **Licence:** Creative Commons BY (open access, attribution).
- **Versioning:** the book targets ISO/IEC 27001:2022 and NIST CSF 2.0 from the outset; standards drift is handled by edition, not errata.

---

## 8. Notes

- Title confirmed: *Substantiate, Don't Assume: Why the Auditor's Opinion Matters More Than Ever in the Age of AI*. (Earlier alternatives, for the record: *Trust, But Verify*; *The Auditor's Edge*; *Judgment Over Automation*.)
- **Drafting happens in this folder.** The Quarto project is scaffolded and written here, mirroring `../conversation-not-delegation/` (one folder per book in the `books/` workspace). See [`README.md`](./README.md) for build and status.
- House style: **no em dashes.** Use periods, colons, semicolons, parentheses, or commas instead. En dashes for number ranges (2022–2026) are fine.
