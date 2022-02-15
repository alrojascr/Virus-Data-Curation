from Bio.SeqIO.FastaIO import FastaIterator, FastaWriter
import argparse
import statistics
import sys

parser = argparse.ArgumentParser(epilog='''''',
                                 description='This script runs the statistics of different fasta files',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-f', '--files', nargs='*', help='Fasta files. Select all fasta files you need to process separated by a space', required=True)
parser.add_argument('-o', '--output', default='sorted.fasta', help='Output name. This name will be used for two files: '
                                                             'output.fasta: it contains the sorted sequences '
                                                             'output.log: it contains a table with all info')
parser.add_argument('-s', '--sort', default=0, choices=[0, 1], type=int, help='Output order. 0- ascendant, 1- descendent')
parser.add_argument('-p', '--print', default=1, choices=[0, 1, 2, 3], type=int,
                                                              help='Define how much info is printed. 0- Print only the summary, 1- Print the longest and shortest'
                                                              ' record per-file, 2- Print the shortest and longest record per-file and 3- Print all stats data for each record and file')

args = parser.parse_args(sys.argv[1:])
# print(args)

# this is the output file for multifasta
sorted_h = open(args.output, "w")
log = open('log.log', 'w')
log.write('  ID  | LENGTH |               SEQ ID                     |         FILE         \n')
# fasta output file handler
gwriter = FastaWriter(sorted_h)

data = {}

stotal = 0
gfsmax = 0
gfsmin = 99999999999
grec_max = []
grec_min = []
gfasta_legth = []
nfiles = 0

# Open the multifasta file

for cfile in args.files:
    nfiles += 1
    if args.print >= 1:
        print(80 * '=')
        print(f'Processing {cfile}...')

    ftotal = 0

    with open(cfile) as fastafile:
        rec_max = None
        rec_min = None
        fasta_legth = []
        fsmax = 0
        fsmin = 99999999999

        for record in FastaIterator(fastafile):
            stotal += 1
            ftotal += 1

            cl = len(record.seq)
            fasta_legth.append(cl)
            if cl > fsmax:
                fsmax = cl
                rec_max = record
            if cl < fsmin:
                fsmin = cl
                rec_min = record
            if cl > gfsmax:
                gfsmax = cl
                grec_max = [cfile, record]
            if cl < gfsmin:
                gfsmin = cl
                grec_min = [cfile, record]

            if args.print == 3:
                print(80 * '-')
                print(record)
                print(80 * '-')
                print('Length: ', cl)


            data[stotal] = [cl, cfile, record]

        gfasta_legth.extend(fasta_legth)
        mean = round(sum(fasta_legth) / len(fasta_legth), 0)

        if args.print >= 1:
            print('')
            print(30 * '*' + '    File Summary    ' + 30 * '*')
            print(f'Number of records: {ftotal}')
            print(f'The average sequences length: {mean}')
            print(30 * '_')

            print(f'Longest record length: {fsmax}')
            if args.print >= 2:
                print(30 * '-')
                print(f'Longest record: {rec_max}')
                print(30 * '_')

            print(f'Shortest record length: {fsmin}')
            if args.print >= 2:
                print(30 * '-')
                print(f'Shortest record: {rec_min}')
                print(30 * '_')
            print('')

if args.sort:
    ordered_list = sorted(data.items(), key=lambda x: x[1][0], reverse=True)
else:
    ordered_list = sorted(data.items(), key=lambda x: x[1][0])
c = 1

for gid, rlist in ordered_list:
    log.write('{:5d} | {:6d} | {:40s} | {:20s}\n'.format(c, rlist[0], rlist[2].id, rlist[1]))
    gwriter.write_record(rlist[2])
    c += 1
    
gmean = round(sum(gfasta_legth) / len(gfasta_legth), 0)

# close the output files
sorted_h.close()

print(80 * '#' + '\n')
print(32 * '#' + '    Summary     ' + 32 * '#')
print(f'Number of files: {nfiles}')
print(f'Number of records: {stotal}')
print(f'The average sequences length: {gmean}')
print(30 * '_')
print(f'Longest global record length: {gfsmax}')
if args.print >= 2:
    print(30 * '-')
    print(f'Longest global record file: {grec_max[0]}')
    print(f'Longest global record: \n{grec_max[1]}')
    print(30 * '_')

print(f'Shortest global record length: {gfsmin}')
if args.print >= 2:
    print(30 * '-')
    print(f'Shortest global record file: {grec_min[0]}')
    print(f'Shortest global record: \n{grec_min[1]}')
    print(30 * '_')
