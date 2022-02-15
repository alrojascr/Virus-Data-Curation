from Bio.SeqIO.FastaIO import FastaIterator, FastaWriter
import argparse
import sys

parser = argparse.ArgumentParser(epilog='''''',
                                            description='This script filters multifasta files',
                                            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', '--files', nargs='*', help='Fasta files. Select all fasta files you need to process separated by a space', required=True)
parser.add_argument('-o', '--output', default='good.fasta', help='Output file containing all filtered fasta')
parser.add_argument('-b', '--badoutput', default='bad.fasta', help='Output file containing bad fasta with the ambiguous nucleotides')
parser.add_argument('-c', '--characters', default="W,S,K,M,Y,R,V,H,D,B,N,-,=", help='Ambiguous characters to filter. Most be string character separated by comma. Example: "N,Y,R,"')
parser.add_argument('-d', '--duplicate', action='store_false', help='Filter duplicate viral sequences showing 100 percent of similarity')
parser.add_argument('-p', '--print', default=1, choices=[0, 1, 2], type=int, help='Define how much info is printed. 0 Print only the summary, 1 Print per-file info and 2, Print all records')

args = parser.parse_args(sys.argv[1:])
# print(args)

# this is the output file for multifasta (good)
good_h = open(args.output, "w")
# this is the output file for multifasta (bad)
bad_h = open(args.badoutput, "w")

# fasta output file handler
gwriter = FastaWriter(good_h)
bwriter = FastaWriter(bad_h)

gbc = 0
ggc = 0
gdc = 0
gtotal = 0

fasta_pool = []

nfiles = 0
# Open the multifasta file

for cfile in args.files:
    nfiles += 1
    if args.print >= 1:
        print(80 * '=')
        print(f'Processing {cfile}...')

    fbc = 0
    fgc = 0
    fdc = 0
    ftotal = 0
    with open(cfile) as fastafile:
        for record in FastaIterator(fastafile):
            print(80 * '-')
            gtotal += 1
            ftotal += 1
            # print each fasta record. (Optional)
            if args.print == 2:
                print(record)
            # check duplicates sequences
            if args.duplicate:
                if not record.seq in fasta_pool:
                    fasta_pool.append(record.seq)
                else:
                    gdc += 1
                    fdc += 1
                    continue
            # Variable for decision
            bad = False
            # Iterate over current fasta sequence
            for nuc in record.seq:
                # Check for invalid nucleotide and gaps
                if nuc in args.characters.split(','):
                    bad = True
            # write this record depending of the context
            if bad:
                gbc += 1
                fbc += 1
                bwriter.write_record(record)
            else:
                ggc += 1
                fgc += 1
                gwriter.write_record(record)
            # reset to default value
            bad = False
            # print(80 * '-')
        if args.print >= 1:
            print('')
            print(30* '*'  + '    File Summary    ' +  30 * '*')
            print(f'Number of records: {ftotal}')
            print(f'Number of bad records: {fbc}')
            print(f'Number of good records: {fgc}')
            if args.duplicate:
                print(f'Number of duplicate records: {fdc}')
            print('')


# close the output files
good_h.close()
bad_h.close()

print(80 * '#' + '\n')
print(32 * '#' + '    Summary     ' + 32 * '#')
print(f'Number of files: {nfiles}')
print(f'Number of records: {gtotal}')
print(f'Number of bad records: {gbc}')
print(f'Number of good records: {ggc}')
if args.duplicate:
    print(f'Number of duplicate records: {gdc}')
