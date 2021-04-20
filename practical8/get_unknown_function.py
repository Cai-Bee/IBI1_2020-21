import os
import re
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
un = open('unknown_function.fa', 'w')

#excute every unknown_function gene data
for i in unknown_seq_data:
    j = i.replace('\n', '$', 1)           # The three steps in the left deleted
    j = j.replace('\n', '')               # all \n expect the first one between
    j = j.replace('$', '\n')              # the discription and the sequence.
    gene_name = re.search(r'gene:(\S*) ?', i).group(1)       #get gene_name from i
    seq = re.search(r'\n(.*$)', j).group(1)                  #get gene sequence
    length = str(len(seq))                                   #measure the sequence's length

    #generate the gene name and length as the new discribe line
    simplified_name = ">" + gene_name + "          " + length
    #generate new data contains thenameofthegene,thelengthofthe encoded protein and the protein sequence
    k = re.sub(r'^.*\]', simplified_name, j) + '\n'
    un.write(k)                           #write unknown_function genes' data into the new file

un.close()
fr.close()
