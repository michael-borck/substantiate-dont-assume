# Substantiate, Don't Assume
## Why the Auditor's Opinion Matters More Than Ever in the Age of AI

**Companion book to ISYS6018 — Information Security Audit and Control (Curtin University)**
**Author:** Michael Borck
**Status:** Chapter outline / proposal (working title)
**Planned format:** Open-access Quarto book, deployed to GitHub Pages (mirroring `michael-borck.github.io/conversation-not-delegation/`)

---

## 1. Why this book

ISYS6018 is standards-driven, not textbook-driven — and that is currently a weakness. The unit's core references are ISO/IEC 27001, NIST CSF, the Privacy Act: authoritative, but not a *narrative* a student can read end to end. There is no spine. *Substantiate, Don't Assume* becomes that spine: a readable, opinionated, open-access core text that the twelve-week course is built around, in the same way ISYS6020 is built around *Conversation, Not Delegation*.

The book solves a second, harder problem. The unit needs to be **AI-aware** — not by bolting "use ChatGPT" onto each lab, but by giving students a coherent stance on what professional judgement is *worth* when machines can draft the technical work. The book is where that stance lives.

---

## 2. The premise: judgement in a commoditised world

The book takes a deliberately pragmatic position on AI — steering clear of both alarmism and techno-utopianism — and lands it on the auditor's desk.

**The commoditisation argument.** The technical craft of information security auditing — enumerating controls, mapping them to frameworks, sampling, drafting test procedures, writing up findings — is exactly the kind of work that generative AI is rapidly commoditising. An AI can list ISO 27001:2022's 93 controls faster and more completely than any junior auditor. If the only thing an auditor does is *produce* that list, the auditor has no edge.

**The variation argument (the human moat).** If an AI is equally good at running every company, then by definition there is no variation between companies that use it generically — and no variation means no competitive edge. The edge comes from variation: human agency, individual taste, a genuine point of view about what matters. For an auditor, that variation shows up as *professional scepticism* — the willingness to look at a polished policy and ask whether the evidence supports it, to decide which of a hundred small gaps actually matters, to form a defensible opinion rather than a confident average. The machine produces the draft; the auditor supplies the judgement. That judgement is the moat.

**From drafter to evaluator.** As AI shifts from chatbots to agentic systems capable of running procedures independently, the auditor's job changes: from creator of "shitty first drafts" to **expert evaluator and editor** of AI-generated work. The unit's assessments already embody this — A2 and A3 require students to document where they *disagreed with or expanded on* AI's analysis. The book makes that discipline explicit and teaches it.

**Augmentation, not automation.** The book's stance is proactive: use these tools for human augmentation and personalised learning — not passive automation that quietly atrophies the critical thinking the profession depends on. Efficiency is not the goal; *defensible judgement* is. If you use AI to skip the thinking, you have done the work wrong, no matter how good the output looks.

This premise is the thread that runs through every chapter.

---

## 3. Design principles

1. **Co-designed with the twelve topics.** Each chapter is one topic: a weekly question (`Why? → Risk? → … → Conclude?`) plus its key concepts. **Chapter *N* = Topic *N*, delivered in Week *N* of the course.** The book and the course deliver the same twelve topics two ways, once to read and once to do. They use different case companies (the book's Tessera companion site, the course's Cloudcore); the topic and its weekly question are the shared spine.
2. **Professional scepticism as the spine.** *Substantiate, don't assume* is stated in the introduction and enacted in every chapter.
3. **One case company throughout the book.** A single case company runs through the book, so every concept lands on a concrete artefact. The book's case company is **Tessera** (on the book's companion site); the course runs the same topics against Cloudcore. The *topic* is shared; the *company* need not be. (Confirmed: Tessera, hosted on the open companion site **tessera.locoensayo.org** under the *LocoEnsayo* rehearsal environments; the course uses Cloudcore.)
4. **AI as a first-class topic, integrated not appended.** Every chapter carries two recurring features (below): one on *using* AI as a thinking partner, one on *auditing* AI where the topic demands it.

---

## 4. Recurring features

Every chapter includes:

- **AI Field Note**: how to use AI as a thinking partner for *this* chapter's task, with a worked example against Tessera. Demonstrates prompt refinement and, crucially, where the AI got it wrong and the auditor corrected it. (This is the book version of the course's weekly **AI Field Notes** task, Assessment 1 Part B. The unit retired BadgeQuest and renamed the weekly AI task accordingly; the book feature name now matches the assessment.)
- **Auditing AI** *(where relevant)* — the chapter's concept applied *to* AI systems: which framework controls an AI deployment falls under, how you audit an AI-assisted control, what evidence an AI system produces.
- **Tessera Case** — a concrete artefact from the Tessera engagement that anchors the chapter.
- **Evidence Locker prompt** — what the student should lock into their cumulative working-paper file this chapter.

---

## 5. Chapter outline

Co-designed with the ISYS6018 twelve-week arc. Two acts: **Engage** (build the case) and **Prove** (from suspicion to proof).

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
Audit objectives, scope, materiality, criteria; the engagement letter; the audit programme; the six-stage audit lifecycle (ISO 19011). The chapter where students learn *how* to audit before *what*. *AI Field Note:* using AI to draft an audit programme — and stress-testing its scope assumptions.

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

## 6. Relationship to the course and to *Conversation, Not Delegation*

- **The book and the course share twelve topics.** The ISYS6018 twelve-week arc and this chapter list cover the same twelve topics, in the same order, each with the same weekly question: **Chapter *N* = Topic *N*, delivered in Week *N*.** A student reads the chapter for a topic in the week they live that topic. The case company can differ between book and course; the *topic* is what is locked in lockstep.
- **The Evidence Locker connects them.** Each chapter's *Evidence Locker prompt* becomes that week's artefact; by Week 12 the locker *is* the Assessment 3 working papers.
- ***Conversation, Not Delegation* is the companion on the AI dimension.** Where *Substantiate, Don't Assume* teaches the audit discipline, *Conversation, Not Delegation* (https://michael-borck.github.io/conversation-not-delegation/) teaches the *how-to-use-AI-well* craft (the trust tool, staying in the loop, compensating for AI's predictable weaknesses). The two are complementary: one is the *what we verify*, the other the *how we work with the machine*. The course links both.

---

## 7. Build and deployment (recommended)

- **Format:** Quarto book (`quarto create-project --type book`), Markdown sources, renders to HTML + PDF + EPUB.
- **Hosting:** GitHub Pages, repo slug `substantiate-dont-assume`, served at `michael-borck.github.io/substantiate-dont-assume/`.
- **Licence:** Creative Commons BY (open access, attribution) — matches Curtin OER practice.
- **Versioning:** the book targets ISO/IEC 27001:2022 and NIST CSF 2.0 from the outset; standards drift is handled by edition, not errata.

---

## 8. Next steps

1. Title confirmed: *Substantiate, Don't Assume: Why the Auditor's Opinion Matters More Than Ever in the Age of AI*. (Earlier alternatives, for the record: *Trust, But Verify*; *The Auditor's Edge*; *Judgment Over Automation*.)
2. **Drafting happens in this folder.** This folder is both the book's spec and its draft home — the Quarto project is scaffolded and written here, mirroring `../conversation-not-delegation/` (one folder per book in the `books/` workspace). See [`README.md`](./README.md) for the handoff and resume instructions. *(Earlier versions of this outline said drafting happened in a separate Quarto project; that was superseded when the folder was relocated into the `books/` workspace. The README is authoritative.)*
3. Scaffold the Quarto book here and write the Introduction + Chapter 1 as the vertical slice, using this outline as the blueprint.
4. Wire the book link into `ISYS6018_outline.md` (done — see Companion Book section).
