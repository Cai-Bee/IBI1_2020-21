#define the function
def rev(seq):
    complement = ""
    #change every base to its reversal base
    for base in seq:
        if base == "A" or base == "a":
            complement += ("T")
        if base == "T" or base == "t":
            complement += ("A")
        if base == "C" or base == "c":
            complement += ("G")
        if base == "G" or base == "g":
            complement += ("C")
        #reverse the list
        l = list(complement)
        new_seq = "".join(l[::-1])
    return new_seq

#example of how this function should be called
seq = 'ATGCGACTACGATCGAGGGCC'
rev(seq)
