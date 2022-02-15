from Bio import SeqIO
import sys
from Bio import AlignIO

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(output_file, "w") as o:
    for record in AlignIO.read(input_file, "fasta"):
        record.seq = record.seq.ungap("-")
        SeqIO.write(record, o, "fasta")