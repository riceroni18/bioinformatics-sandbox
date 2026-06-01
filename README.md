# Bioinformatics Sandbox & Engineering Archive

Welcome to my technical playground! This repository serves as a centralized, curated archive for independent scripts, algorithm prototypes, and containerized pipeline contributions. It tracks my practical application of computational biology concepts, data optimization, and structural genomic engineering.

---

## 📁 Repository Directory

Click into any project folder below to view specific source code, execution workflows, and sample outputs.

### 1. 🧬 [DNA Sequence Parser & Visualizer](./dna_sequence_parser)
* **Description:** A Python utility that automates basic quality control (QC) checks on raw nucleotide inputs.
* **Core Function:** Leverages Biopython to parse multi-record FASTA files, compute precise sequence-specific GC-content metrics, and export publication-ready distribution bar charts using Matplotlib.

### 2. 🤖 [Human Phenotype Ontology (HPO) Data Mapper](./hpo_data_mapper)
* **Description:** An NLP-adjacent clinical text-mining tool that standardizes phenotype entries for downstream variant prioritization.
* **Core Function:** Ingests dictionary-based reference ontologies via JSON, tokenizes and normalizes unstructured clinical notes, and outputs structured mappings of matched medical conditions to their official HPO IDs.

### 3. 🚀 [Microbial Gene Prediction Pipeline (Prodigal)](./gales_pipeline)
* **Description:** A Linux-based environment execution wrapper focused on automated structural annotation workflows.
* **Core Function:** Features a Bash automation shell script (`run_prodigal.sh`) that streamlines parameter passing for the Prokaryotic Dynamic Programming Genefinding Algorithm to map genetic features and export standardized GFF files.

### 4. 🤝 [Open-Source Contribution: nf-core/seqsubmit Validation Utility](./vibiome_hackathon)
* **Description:** Production-grade validation script and defensive programming layers built for collaborative, community-driven workflows.
* **Core Function:** Extends `submit_study.py` to normalize and validate tabular CSV/TSV metadata arrays using set operations before pushing payloads to the European Nucleotide Archive (ENA) Webin REST API v2.

---

## 🛠️ Unified Core Tech Stack

* **Languages:** Python 3 (Pandas, Biopython, Matplotlib, Requests, Click), Bash Scripting, Nextflow
* **Environments & Infrastructure:** Linux / Windows Subsystem for Linux (WSL), Docker
* **Data Standards:** FASTA, GFF, JSON, CSV/TSV, XML, HPO (Human Phenotype Ontology)

---

## 📈 Portfolio Architecture Strategy
Unlike comprehensive production-level repositories that use heavily nested folder segments, this sandbox utilizes a **flat-grouping layout** within individual directories. Each micro-project isolates its source code, markdown documentation, and lightweight mock inputs/graphical results in a single layer to facilitate rapid code review and immediate architectural visibility.
