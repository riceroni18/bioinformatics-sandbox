import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

print("Script is starting...")

def analyze_and_visualize_gc(filename):
    gc_values = []
    labels = []

    # Using Biopython for  parsing
    for record in SeqIO.parse(filename, "fasta"):
        # gc_fraction returns a value between 0 and 1
        gc = round(gc_fraction(record.seq) * 100, 2)
        gc_values.append(gc)
        labels.append(record.id)
        print(f"Sequence: {record.id} | GC: {gc}%")

    # Creating the Visualization
    plt.figure(figsize=(10, 6))
    plt.bar(labels, gc_values, color='skyblue', edgecolor='navy')
    plt.axhline(y=sum(gc_values)/len(gc_values), color='red', linestyle='--', label='Mean GC')
    
    plt.title("GC Content Distribution Across Sequences", fontsize=14)
    plt.xlabel("Sequence Identifier", fontsize=12)
    plt.ylabel("GC Content (%)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
    #generate graph
    plt.savefig("gc_distribution_graph.png")
    print("Graph saved as gc_distribution_graph.png") # Added a confirmation print


# Make sure to replace "sequences.fasta" with your actual filename!
analyze_and_visualize_gc("sequences.fasta")