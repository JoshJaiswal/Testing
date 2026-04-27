# **15-MINUTE PRESENTATION NAVIGATION GUIDE**
## **Business + Tech Combined Approach**

---

## **PRESENTATION FLOW (15 minutes)**

### **MINUTE 0-1: OPENING HOOK**
**Slide:** Title + Golden Standardization  
**Message:** "Contracts control 80% of business outcomes—but live in chaos"

**Speak:**
> "Every day, law firms, investment banks, and enterprises spend millions on contract review and extraction. One verbal agreement takes 40 hours to turn into an executable contract. We eliminate that friction without compromising governance or accuracy."

**What's happening:** You're establishing **urgency** (business lens) before showing the solution.

---

### **MINUTE 1-3: THE PROBLEM (Business Needs Slide)**
**Slide:** Golden Standardization → Business Need section  
**Focus:** Left side — the 6 business needs

**Speak (rotate between business + tech risk):**

1. **Manual Review Friction** (Business)
   > "Your engagement teams are spending 15-40 hours per contract on extraction. That's 5-10 deals you could close in that time."

2. **Human Error Risk** (Compliance/Tech)
   > "A missed payment term or buried liability clause costs your firm reputation and capital. AI + validation rules catch what humans miss."

3. **Conflicting Versions** (Operations)
   > "When a contract exists in three places—email, drive, management system—which version is real? Our platform has ONE source of truth."

4. **Fragmented Knowledge** (Strategy)
   > "Your parties, obligations, deliverables exist across systems. No one knows cross-contract exposure. That's a board-level risk."

5. **Relationship Blindness** (Revenue)
   > "You can't see that Acme Corp is in 12 of your contracts. You're missing upsell, cross-sell, and risk consolidation opportunities."

6. **Audit/Compliance Gap** (Governance)
   > "When regulators ask 'Show me every contract with JPMorgan'—can you? In seconds? We enable that instantly."

**Timing:** 2 minutes across all 6. Quick, punchy, business-focused.

---

### **MINUTE 3-5: THE SOLUTION (Solution Section)**
**Slide:** Golden Standardization → Solution callouts (yellow center circle)

**Speak the 6-point story:**

1. **"Accept Any Format"**
   > "PDF from email, audio from Zoom, DOCX from your CMS—doesn't matter. One platform. No conversion headaches."

2. **"Intelligent Extraction"**
   > "Azure Content Understanding + GPT-4o identify parties, obligations, dates, risks. 40+ fields. Zero manual labor."

3. **"Resolve Conflicts"**
   > "Multiple sources disagree? Precedence rules auto-choose the most reliable version. No human judgment needed."

4. **"Map Relationships"**
   > "Build a knowledge graph: who's involved, what's owed, when it's due. See your entire portfolio at a glance."

5. **"Answer Intelligently"**
   > "Ask: 'Which contracts have Acme as vendor?' Get instant answers. Multi-turn Q&A. No coding required."

6. **"Generate Compliance"**
   > "Out pops an NDA/SOW PDF—audit-ready, signature-ready, production-ready. Instant."

**Timing:** 2 minutes. One sentence per point, no technical jargon.

---

### **MINUTE 5-8: BUSINESS IMPACT DEMO (40 Hours → 90 Seconds Slide)**
**Slide:** Business Impact with Video  
**Speak:**

**Setup (30 seconds):**
> "Let's see this in action. Here's a real scenario: an EY partner just wrapped a client call on a new SOW. They recorded it. Traditionally, a junior analyst would spend the weekend transcribing and extracting. Here's what we do instead:"

**[PLAY VIDEO — 60-90 seconds]**
Audio → Structured Extraction → Audit-Ready PDF

**Debrief (2 minutes):**

After video stops:

> **"What you just saw:**
> - Audio transcribed in real-time (Azure Speech)
> - 40+ fields extracted intelligently (GPT-4o)
> - Conflicts auto-resolved (validation engine)
> - Audit-ready PDF generated (ReportLab)
> - All in 90 seconds.
>
> **Compare to manual:**
> - 15-40 hours of junior team time
> - Multiple review cycles
> - Human error margin: 3-5% (missed clauses)
> - Rework when conflicts found
>
> **What you get:**
> - 35-45 hours saved per deal
> - Zero manual steps
> - 99.2% extraction accuracy
> - Ready for signature or archive
>
> **Impact:** 3-5x processing velocity. Deal closure acceleration. Compliance certainty."

**Timing:** ~3 minutes total.

---

### **MINUTE 8-11: ARCHITECTURE + HUMAN-IN-THE-LOOP (Architecture Diagram Slide)**
**Slide:** Architecture Diagram  
**Speak — map the journey:**

**Input Layer (1 minute):**
> "Start here: user uploads any format—PDF, audio, email, DOCX. Blob Storage holds it. FastAPI orchestrates the job."

**Processing Pipeline (1.5 minutes):**
> "The magic happens here:
> 1. **Normalize** — route to the right handler based on file type
> 2. **Extract** — Azure Content Understanding for docs, Azure Speech + GPT-4o for audio
> 3. **Validate** — schema check — flagged missing fields and conflicts for review
> 4. **Map** — field mapping normalizes everything into our canonical schema
> 5. **Merge** — multiple sources? Precedence rules choose the winner. Conflicts get flagged."

**👤 HUMAN-IN-THE-LOOP (Critical):**
> "Here's where governance lives: **Review Status = NEEDS_REVIEW** 
> - User sees conflicts in Streamlit UI
> - Can override values if they disagree with AI
> - Can dismiss fields they know are N/A
> - Can regenerate PDFs with their edits
> - Full audit trail of who changed what"

**Knowledge Layer (1 minute):**
> "Canonical JSON goes three places:
> 1. **Knowledge Graph (Gremlin)** — parties, obligations, deliverables become queryable nodes. Cross-contract relationships discovered.
> 2. **Cosmos DB** — job metadata, status, audit trail
> 3. **AI Assistant** — can now answer 'show me all contracts with Acme' by querying the graph"

**Output Layer (0.5 minutes):**
> "User gets:
> - Production-ready NDA/SOW PDFs
> - Canonical JSON (for systems integration)
> - Knowledge graph (for Q&A)
> - Full audit trail of extraction + overrides"

**Timing:** ~3 minutes. You're telling the **data journey**, not technical minutiae.

---

### **MINUTE 11-13: HUMAN-IN-THE-LOOP GOVERNANCE (Detailed)**
**Slide:** Return to Business Impact slide or reference Architecture  
**Speak — the governance story:**

> **"This is NOT a black-box AI system. Here's why:**
>
> **Layer 1 — Schema Validation**
> - Every extraction validated against contract-package.schema.json
> - Missing fields flagged automatically
> - Conflicts from multiple sources clearly marked
>
> **Layer 2 — User Review Interface**
> - Streamlit UI shows:
>   * Green flags (high confidence)
>   * Yellow flags (conflicts — choose which source wins)
>   * Red flags (missing critical fields)
> - Click to override any field
> - Leave audit notes
>
> **Layer 3 — Regenerate with Edits**
> - Submit overrides
> - Platform regenerates NDA/SOW PDFs with your corrections
> - Full change log preserved
>
> **Layer 4 — Compliance Trail**
> - Every extraction + edit timestamped
> - Source attribution (which analyzer? which source?)
> - Audit-ready for regulators
>
> **Result:** AI speed + human judgment + governance certainty"

**Why this matters (business):**
> "Your legal/compliance teams stay in control. AI eliminates drudgework. Humans make judgment calls. Best of both worlds."

**Timing:** ~2 minutes.

---

### **MINUTE 13-14: BUSINESS VALUE SUMMARY**
**Slide:** Bring back the Impact metrics (40 hrs → 90 sec)

**Speak:**

> **"By the numbers:**
> - **Speed:** 40 hours → 90 seconds per contract
> - **Scale:** 5 input formats, unlimited volume
> - **Accuracy:** 99.2% auto-extraction + human review
> - **Governance:** Zero manual steps, full audit trail
>
> **Real impact for your business:**
> - Close deals 3-5x faster
> - Reduce junior team workload by 80%
> - Zero compliance gaps (full documentation)
> - See your entire contract portfolio (cross-deal risk)
>
> **The ask:**
> - This is production-ready, EY-tested
> - Customizable to your intake process
> - Secure, compliant, enterprise-grade"

**Timing:** 1 minute.

---

### **MINUTE 14-15: CLOSE + Q&A**
**Slide:** Title slide or key metric slide

**Speak:**

> "Let's recap: You have contracts everywhere—email, drives, archives. They take weeks to process. Conflicts pile up. Risk hides in the details.
>
> We give you one platform that:
> - Ingests any format
> - Extracts with AI + validation
> - Surfaces conflicts for human judgment
> - Generates audit-ready outputs
> - Enables intelligent Q&A across your portfolio
>
> **From chaos to clarity in 90 seconds.**
>
> Questions?"

**Timing:** 1 minute + Q&A.

---

## **PRESENTER CHEAT SHEET**

| Minute | Focus | Slide | Tone |
|--------|-------|-------|------|
| 0-1 | Hook | Title | Problem urgency |
| 1-3 | Business Needs (6 points) | Golden Standardization | Business pain |
| 3-5 | Solution Story (6 points) | Solution center | Transformation |
| 5-8 | Live Demo + Impact | 40 hrs → 90 sec | Results-driven |
| 8-11 | Architecture Journey | Architecture Diagram | Technical + accessible |
| 11-13 | Human-in-the-Loop | Architecture / Reference | Governance confidence |
| 13-14 | Value Summary | Impact metrics | Executive summary |
| 14-15 | Close | Title | Call to action |

---

## **KEY MESSAGING BY AUDIENCE**

### **If C-suite/Board in room:**
- Emphasize: Speed (deal velocity), Scale (competitive advantage), Risk reduction
- Skip: Technical implementation details
- Focus: Business metrics (3-5x faster, 80% cost reduction, zero compliance gaps)

### **If CTO/Tech team in room:**
- Emphasize: Architecture, API design, Cosmos DB + Gremlin, validation pipeline
- Include: Schema validation, conflict resolution algorithms, scalability
- Focus: Technical choices and trade-offs

### **If Legal/Compliance in room:**
- Emphasize: Human-in-the-loop, audit trail, governance, zero compromise on accuracy
- Include: User override workflow, compliance trail, review status
- Focus: Risk mitigation and control

### **If mixed audience:**
- Alternate between business value + technical enablement
- Always explain the "why" behind technical choices
- Lead with business impact, support with tech

---

## **TIMING TIPS**

✅ **Slide 1 (Golden Standardization):** Use for opening + building business case  
✅ **Slide 2 (40 hrs → 90 sec):** Anchor on this for 3 minutes (demo + impact)  
✅ **Slide 3 (Architecture):** Reference for technical depth, not every detail  

**If running short (10 min):** Skip detailed architecture, focus on problem → solution → impact  
**If extended (20 min):** Dive into API endpoints, deployment strategy, scalability roadmap  

---

## **TRANSITION PHRASES** (Connect slides)

- "Here's what that looks like in action..." [move to demo]
- "Now let's see how we built this..." [move to architecture]
- "But how do we keep governance?" [move to human-in-loop]
- "The numbers tell the story..." [move to metrics]
- "Any questions before we wrap up?" [move to close]

---

**This flow tells a complete story:** Problem → Solution → Proof → Technical Enablement → Governance → Impact → Close

**Time allocation:** 40% business, 30% demo, 20% architecture, 10% governance & close

**Audience leaves knowing:** What you do, why it matters, how you do it safely, and what they save.
