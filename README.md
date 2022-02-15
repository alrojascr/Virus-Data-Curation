# **TOOLS FOR FILTERING VIRUS DATA**


Suite of tools for filtering, processing and matching viral sequences retrieved from major databases including [National Center for Biotechnology Information Virus (NCVI Virus)](https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/), [Virus Pathogen Database and Analysis Resource (ViPR)](https://www.viprbrc.org/brc/home.spg?decorator=vipr), [ViruSurf]( http://geco.deib.polimi.it/virusurf/) and [Global Initiative on. Sharing All Influenza Data (GISAID)]( https://www.gisaid.org/). 



| Program                    | Description                                                                                                    |
|:-------------------------  |:-------------------------------------------------------------------------------------------------------------- |
|fa-curator                  | This program filters each viral sequence retaining the unambiguous                                             |                                                 |                            | nucleotides: `A, C, G, T` and, parallelly, compares them across different databases to remove those showing    |                             |                            | 100% similarity and return a single sequence for constituting a non-redundant dataset.                         |                                        
|fa-cleaner                  | This tool is suitable for removing viral sequences from a dataset through the length and `N` percentage of     |
|                            | sequences to be filtered.                                                                                      |
|fa-extract                  | The purpose of this program is to extract sequences in a fasta file depending on keywords included in the      |
|                            | header. The keyword string can be partial or complete.                                                         |
|fa-rename                   | A very useful script to rename sequence headers in a fasta file.                                               |
|fa-stats                    | This is a program for sorting sequences from the shortest or vice versa, listing length for each sequence      |
|                            | and overall average of the entire dataset through multiple fasta files.                                        |
|fa-ungap                    | This is a script converts a multiple sequence alignment to a fasta format file, removing all gaps.             |



## **Pre-requisites**


To run these tools the following must be installed:

-	Python 3.8 or later



## **Running**



### **fa-curator**

```
fa-curator.py --files <NCBI.fa ViPR.fa GISAID.fa> --output <good.fa> --badoutput <bad.fa> --characters < "W,S,K,M,Y,R,V,H,D,B,N,-,="> --duplicate --print [0, 1, 2]
```



### **fa-cleaner**

```
fa-cleaner.py fasta_file min_length max_length

```



### **fa-extract**

```
fa-extract.py --fasta <file.fa> --string <"SARS"> --outfile <out.fa> --verbose --invert --method ["exact", "partial"]
```



### **fa-rename**

```
fa-rename.py [--tab new_names.txt] FASTA > out.fa
```



### **fa-stats**

```
fa-stats.py --files <file1.fa file2.fa file3.fa> --output <"output.fa" "output.log"> --sort [0, 1]
--print [0, 1, 2, 3]
```



### **fa-ungap**

```
fa-ungap.py input.fa output.fa
```



## **License**

The python tools are released under the MIT License.
