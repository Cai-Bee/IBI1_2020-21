#define a function that chanslate codon to proteinsequence
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
        #find the codon in the dictionary and return its corresponding amino acid
        if sequence[n:n + 3] in codonTable.keys():
    #add recognized amino acid to the proteinsequence
            proteinsequence += codonTable[sequence[n:n + 3]]
    return proteinsequence

#create the string variable seq
seq = 'ATGCGACTACGATCGAGGGCC'
print('The amino acid sequence is: '+translate_dna(seq))
