# DNA Sequence Parser & GC Content Visualizer

A lightweight Python utility designed to parse raw multi-FASTA files, calculate sequence-specific GC-content percentages, and generate data visualizations. This script automates basic quality control (QC) checks on incoming nucleotide sequences prior to downstream genomic workflows.

## 🧬 Key Features
* **Automated FASTA Parsing:** Leverages Biopython's `SeqIO` engine to smoothly parse multi-record sequence files.
* **GC-Content Analytics:** Computes exact GC percentages per sequence header using optimized sequence-utility matrices.
* **Dynamic Visualization:** Generates and saves a customized bar chart (`gc_distribution_graph.png`) showing the distribution across all records, complete with an automated mean line for baseline cohort analysis.

---

## 💻 Tech Stack & Dependencies
* **Language:** Python 3
* **Libraries:** 
  * `Biopython` (For robust sequence parsing and data handling)
  * `Matplotlib` (For data visualization and image exporting)

To install the required dependencies, run:
```bash
pip install biopython matplotlib
