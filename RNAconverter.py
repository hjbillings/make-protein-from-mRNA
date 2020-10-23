"""
@hjbillings
problem from the Rosalind project

Given: An RNA string corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by the RNA.
"""

def makeProtein(sequence, codon_aa_table):
    i=0
    j=3
    length=len(sequence)
    protein = []
    for i in range(0, length, 3):
        codon = sequence[i:i+3]
        aa = ""
        aa += codon_aa_table[codon]
        protein.append(aa)
    return("".join(protein))

sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
codon_aa_table = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
            'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
            'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
            'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',                                                           
            'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S',
            'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
            'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
            'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
            'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop',
            'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
            'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
            'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
            'UGC':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W',
            'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
            'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
            'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',}
print(makeProtein(sequence, codon_aa_table))