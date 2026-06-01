# Microbial Gene Prediction Pipeline (Prodigal)

This project documents the execution of structural gene prediction workflows within a containerized Linux environment. It features a automation shell script designed to process raw bacterial assemblies and output standardized genomic feature files.

## 🛠️ Infrastructure & Tools
* **Workflow Environment:** Linux / WSL
* **Gene Predictor:** Prodigal (Prokaryotic Dynamic Programming Genefinding Algorithm)
* **Target Data:** *E. coli* bacterial genome assembly

---

## 🚀 Pipeline Script (`run_prodigal.sh`)
The core execution is driven by a lightweight bash script that automates the command-line parameters for the algorithm:

```bash
#!/bin/bash
# Script to run gene prediction using Prodigal
prodigal -i data/unit2_new_genome.fasta -o data/unit2_new_genome.prodigal.gff -f gff

echo "Gene prediction complete. Output saved to data/unit2_new_genome.prodigal.gff"
