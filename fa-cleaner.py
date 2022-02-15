import sys
from Bio import SeqIO

def extract_seq(fasta_file, min_length=0, max_length=16000):
    # Create our list to add the sequences
    sequences = []
    # Using the Biopython fasta parse we can read our fasta input
    for seq_record in SeqIO.parse(fasta_file, "fasta"):
        # Take the ID and sequence
        sequence_id = (seq_record.id)
        sequence = str(seq_record.seq).upper()
        # Check if the current sequence is according to the user parameters
        if (len(sequence) >= min_length and
        (len(sequence) <= max_length)):
            sequences.append(sequence_id + "\n" + sequence)

    # Write the sequences

    # Create a file in the same directory where you ran this script
    with open("extract_" + fasta_file, "w+") as output_file:
        # Just read the list and write on the file as a fasta format
        for sequence in sequences:
            output_file.write(">" + sequence + "\n")

    print("Please check extract_" + fasta_file)


userParameters = sys.argv[1:]

try:
    if len(userParameters) == 1:
        extract_seq(userParameters[0])
    elif len(userParameters) == 2:
        extract_seq(userParameters[0], int(userParameters[1]))
    elif len(userParameters) == 3:
        extract_seq(userParameters[0], int(userParameters[1]),
                         int(userParameters[2]))
    else:
        print("There is a problem!")
except:
    print("There is a problem!")