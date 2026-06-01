# Open-Source Contribution: nf-core/seqsubmit Metadata Validator

This folder archives a verified open-source utility script developed and modified as part of a collaborative feature addition to the official **nf-core/seqsubmit** pipeline—a community-driven Nextflow workflow designed to automate the submission of genomic data to INSDC databases (ENA, NCBI, DDBJ).

**🔗 Verified Contribution:** [nf-core/seqsubmit Commit d36f21e](https://github.com/nf-core/seqsubmit/commit/d36f21ee76c9a8ac5bb7d22d51e31288b3742d5b)

---

## 🛠️ Feature Overview: `submit_study.py`
In automated high-throughput data curation environments, structural errors or malformed columns in tabular input metadata frequently crash expensive downstream processing runs. My contribution focused on establishing an explicit data-ingestion validation layer and clean logging structure within `submit_study.py` to intercept errors gracefully.

### Key Engineering Details:
* **Robust Column Validation:** Engineered a defensive header normalization block inside `load_and_validate_input_file()` that maps delimiter variations across CSV and TSV formats, strips hidden whitespace/quotes, and executes set evaluations against `_REQUIRED_FIELDS` (`alias`, `study_title`).
* **Production Logging Infrastructure:** Leveraged Python's standard `logging` module to direct error streams out to `sys.stderr`, replacing silent failures with highly descriptive operational alerts detailing exactly which columns are missing.
* **Safe Ingestion Dictionaries:** Implemented fallback dictionary handling (`.get()`) within the reporting summary sequence to guarantee the validation script cleanly logs batch status information even if key accessions are pending from the API server.

---

## 💻 Tech Stack & Pipeline Ecosystem
* **Core Language:** Python 3 (Typing, Click, Requests, ElementTree XML)
* **Target Automation Platform:** Nextflow (DSL2 Framework)
* **Target Repositories:** European Nucleotide Archive (ENA Webin REST API v2)
* **Design Philosophy:** PEP 8 Compliance, Object-Oriented Exception Handling, and Defensive Programming
