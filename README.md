# 🏠 Detailed Diagnostic Report (DDR) Generator

## Applied AI Builder Assignment – Option A

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Gemini](https://img.shields.io/badge/Gemini-2.5%20Flash-orange)
![Architecture](https://img.shields.io/badge/Design-Multi--Stage-green)

---

<div align="center">

### 🚀 Converting Raw Inspection + Thermal Reports → Structured Client-Ready DDR

**Assignment Focus:** System Thinking • Reliability • No Hallucinations • Structured AI Workflow

🎥 **Loom Walkthrough:**
[https://www.loom.com/share/bb3ca12a7b274b9f9c7595d2de9199db](https://www.loom.com/share/bb3ca12a7b274b9f9c7595d2de9199db)

</div>

---

# 📌 Assignment Objective

Build an AI system that:

* Reads **Inspection Report**
* Reads **Thermal Report**
* Extracts relevant findings
* Merges them logically
* Detects missing/conflicting information
* Generates a structured **7-section Detailed Diagnostic Report**
* Avoids hallucinations
* Uses simple client-friendly language

---

# 🏗️ System Architecture (Designed for Reliability)

This solution intentionally avoids single-prompt generation.

Instead, it uses a **multi-stage AI workflow**:

```
PDF Upload
    ↓
Text Extraction Layer
    ↓
Structured JSON Extraction (Inspection + Thermal separately)
    ↓
Deterministic Merge Logic (Python)
    ↓
Conflict & Missing Data Detection
    ↓
Controlled DDR Generation (Strict Template)
    ↓
Compliance Validation
```

### Why this matters:

* Prevents hallucination
* Enables structured reasoning
* Handles imperfect data
* Generalizes to similar reports
* Shows production-level system thinking

---

# 🧠 Core Design Decisions

## 1️⃣ Structured Intermediate Layer

Instead of generating DDR directly from raw text:

* Inspection report → Converted to structured JSON
* Thermal report → Converted to structured JSON
* Merged programmatically before final generation

This ensures:

* No duplicate entries
* Explicit area mapping
* Conflict detection possible

---

## 2️⃣ Anti-Hallucination Guardrails

Strict enforcement in prompt:

* “Do NOT invent facts”
* Missing fields → must output `"Not Available"`
* Conflicts → explicitly mention
* No assumptions allowed

This aligns directly with assignment constraints.

---

## 3️⃣ Deterministic Merging Logic

* Fuzzy area matching (RapidFuzz)
* Programmatic conflict detection
* Missing thermal data flagged automatically

The LLM does reasoning.
The system enforces structure.

---

# 📊 Output Structure (Exactly as Required)

Generated DDR always contains:

1. Property Issue Summary
2. Area-wise Observations
3. Probable Root Cause
4. Severity Assessment (with reasoning)
5. Recommended Actions
6. Additional Notes
7. Missing or Unclear Information

No deviations. No freestyle formatting.

---

# ⚙️ Tech Stack

* **Python 3.9+**
* **Gemini 2.5 Flash**
* **Streamlit**
* **pdfplumber**
* **RapidFuzz**
* **dotenv for secure API management**

---

# 🚀 Installation

```bash
git clone https://github.com/Tanmay1112004/Detailed-Diagnostic-Report--DDR--Generator.git
cd Detailed-Diagnostic-Report--DDR--Generator

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

Create `.env`:

```
GEMINI_API_KEY=your_api_key_here
```

Run:

```bash
streamlit run app.py
```

---

# 📋 Assignment Evaluation Criteria – Covered

| Requirement                   | Implementation                       |
| ----------------------------- | ------------------------------------ |
| Extract relevant observations | Structured extraction layer          |
| Combine inspection + thermal  | Deterministic merge logic            |
| Avoid duplicates              | Programmatic deduplication           |
| Handle missing data           | Explicit `"Not Available"` insertion |
| Handle conflicts              | Severity mismatch detection          |
| Client-friendly language      | Prompt constraints                   |
| No hallucinations             | Guardrails + validation              |
| Generalizable                 | No hardcoded area names              |

---

# 🔬 Reliability Considerations

* Missing thermal mapping explicitly flagged
* Conflict detection between severity indicators
* No inference beyond document evidence
* Clean separation between extraction & generation
* Structured intermediate artifacts available for review

---

# 📉 Known Limitations

* Area matching depends on naming similarity
* Thermal report lacks precise image-to-room mapping
* PDF extraction quality impacts structured accuracy
* No OCR for scanned PDFs (future enhancement)

---

# 🔮 Future Improvements

With additional time:

* Confidence score per area
* Vector-based semantic area matching
* OCR support
* PDF/DOCX export formatting
* Batch processing for multiple properties
* Human-in-the-loop review layer

---

# 🎯 Why This Solution Demonstrates Applied AI Thinking

This project was built to reflect:

* Multi-stage AI workflow design
* Structured reasoning over raw prompting
* Deterministic + LLM hybrid architecture
* Guardrail-driven generation
* Production-aware system design

It focuses on **reliability and system thinking**, not just calling an API.

---

# 👤 Candidate

**Tanmay**
AI Generalist | Applied AI Builder

Assignment Completed Within 24 Hours
All Requirements Met

---

<div align="center">

### ⭐ Built with engineering discipline, not just prompts ⭐

</div>

---
