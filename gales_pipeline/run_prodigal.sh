#!/bin/bash
# Script to run gene prediction using Prodigal
# -i: input sequence (FASTA)
# -o: output annotation (GFF)
# -f: specify GFF output format

prodigal -i data/unit2_new_genome.fasta -o data/unit2_new_genome.prodigal.gff -f gff

echo "Gene prediction complete. Output saved to data/unit2_new_genome.prodigal.gff"
