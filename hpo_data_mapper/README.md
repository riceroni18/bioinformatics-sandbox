# Human Phenotype Ontology (HPO) Data Mapper

A specialized Python utility designed to parse unstructured clinical text and map phenotypic medical descriptions directly to standardized **Human Phenotype Ontology (HPO)** codes. This tool mimics the core text-mining logic used in high-throughput diagnostic workflows to standardize patient data for downstream genomic analysis.

## 🧬 Key Features
* **Robust JSON Ingestion:** Safely handles error-catching and validation when loading large dictionary-based ontology master files (`hpo_data.json`).
* **Text Normalization Engine:** Strips out structural noise, punctuation, and casing discrepancies to ensure uniform string matching against reference databases.
* **Dictionary-Based Term Mapping:** Evaluates tokenized clinical strings against reference datasets to generate clean, key-value mappings of matched phenotypes and their official HPO IDs.

---

## 💻 Tech Stack & Dependencies
* **Language:** Python 3
* **Libraries:** 
  * `json` (Built-in standard library for high-performance key-value data structures)

No external third-party installations are required to run this utility.

---

## 🚀 How to Run the Script

1. Ensure your dictionary file containing the HPO codes is named `hpo_data.json` and resides in the same folder as the script.
2. Execute the mapper via your terminal:

```bash
python hpo_mapper.py
