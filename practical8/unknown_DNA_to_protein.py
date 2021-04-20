#get name input
print("please input a filename as the new fasta file to be written to")

name = input("File name?")

import os
import re
#define a function that translates codon to proteinsequence
def translate_dna(sequence):
    #create a dictionary. codons are keys, proteins are value
    codonTable = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA':  '', 'TAG':  '',
        'TGC': 'C', 'TGT': 'C', 'TGA':  '', 'TGG': 'W',
    }
    # dim proteinsequence as a string
    proteinsequence = ''
    #select every three letters and recognize them as a codon
    for n in range(0, len(sequence), 3):
        if sequence[n:n + 3] in codonTable.keys():
    #add newly recognized codon to the proteinsequence
            proteinsequence += codonTable[sequence[n:n + 3]]
    return proteinsequence

#This work when operating in terminal
os.chdir('/Users/caishuo/github/IBI1_2020-21/practical8')
import sys
#This work when running as a module
os.chdir(sys.path[0])

#read data from the initial fatsa document
fr = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
data = fr.read()


#find all gene data with the discription 'unknown function'.
unknown_seq_data = re.findall(r'[^>]+unknown.function[^>]+', data)

#create a new object to contain selected and changed data
un = open(name, 'w') #'w'means 'writing mode'

#excute every unknown_function gene data
for i in unknown_seq_data:
    j = i.replace('\n', '$', 1)           # The three steps in the left deleted
    j = j.replace('\n', '')               # all \n expect the first one between
    j = j.replace('$', '\n')              # the discription and the sequence.
    gene_name = re.search(r'gene:(\S*) ?', i).group(1)       #get gene_name from i
    seq = re.search(r'\n(.*$)', j).group(1)
    pro_seq = translate_dna(seq)                             #get proteins' sequences
    length = str(len(pro_seq))                               #get proteins' sequence length
    j = re.sub(r'[^\n]+$', pro_seq, j)
    simplified_name = ">" + gene_name + "          " + length
    k = re.sub(r'^.*\]', simplified_name, j) + '\n'          #generate the gene name and protein sequence's length as the new discribe line
    un.write(k)                           #write unknown_DNA_to_protein data into the new file

un.close()
fr.close()
