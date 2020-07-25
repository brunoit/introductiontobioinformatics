# we somehow have to read in in the DNA string
dna_string = 'GCGGGGATCGATAAACCTAACTCCACGATCGTTCTTCGGACTATCTTACCCAGGGAAAAATAGAGGCATCTTTCCAGCAATAAACCGAATTCGCCGTTCTTATATAGGAGTCCGAACGTGTTGGGATTCTGTTTCGCCCTGTCCTATCGTGCGATATCTAAGAAAACCCCTCACTGCAAGTAAAAGATTGTTGGAAAGATTGATGGCGCATGACTGGCAGGACAATAGAGCCCCCATGGGAACCATGGAGATGATGAGAGCGTCCTGAGAATGATTACCGCGACAATTCCGAGTTTAAGGGCCGCCCAGCATTATATTGTCAGCCGAGTCTGGTGTGTGAACAGCCCGAACACTGGGGCCGAGGGAACCTGCAACCTTTAAAATGTAAAAAATGAGGCGCCATGTAGATGGCGTTGGACTAATTATTCCGATCGGAAAAACTCCTAAAGAGGGCTCGAATCTTGTGTGGGGGGGCGGCCTTAATAACATCGGTGGTCAACGTCAAGTACGCGGCACCTATTGCAATGTCAAGCTATATTATCTACCTTGACTGAAAGACACCCTATAAATGGCCAAACAATCCACGACAACAGTTCACTAGGTGATGGATAACCCTGTGTACCAGCCCTCTTGTCGGTAGTAGAGCGGGAAAGCTGTGATGCTTATCTGTGCGATGGGGTGTAACGATCCCTTACCACGACAGACGCTGCAACGCCGCACCATATCCCTTAGTCCCATGTTCTAGTTCCCGCCAGTACAAGGCAATTCATATGACAAGATGGACTTTGCCCCGGTAGGGACGTTGGACTCCCACCAGATCCTCGCTATCCTATGCTATTCCTGTAAACACATGGTGCCATATTCAGGCGTGCGCGGGGATCGATAAACCTAACTCCACGATCGTTCTTCGGACTATCTTACCCAGGGAAAAATAGAGGCATCTTTCCAGCAATAAACCGAATTCGCCGTTCTTATATAGGAGTCCGAACGTGTTGGGATTCTGTTTCGCCCTGTCCTATCGTGCGATATCTAAGAAAACCCCTCACTGCAAGTAAAAGATTGTTGGAAAGATTGATGGCGCATGACTGGCAGGACAATAGAGCCCCCATGGGAACCATGGAGATGATGAGAGCGTCCTGAGAATGATTACCGCGACAATTCCGAGTTTAAGGGCCGCCCAGCATTATATTGTCAGCCGAGTCTGGTGTGTGAACAGCCCGAACACTGGGGCCGAGGGAACCTGCAACCTTTAAAATGTAAAAAATGAGGCGCCATGTAGATGGCGTTGGACTAATTATTCCGATCGGAAAAACTCCTAAAGAGGGCTCGAATCTTGTGTGGGGGGGCGGCCTTAATAACATCGGTGGTCAACGTCAAGTACGCGGCACCTATTGCAATGTCAAGCTATATTATCTACCTTGACTGAAAGACACCCTATAAATGGCCAAACAATCCACGACAACAGTTCACTAGGTGATGGATAACCCTGTGTACCAGCCCTCTTGTCGGTAGTAGAGCGGGAAAGCTGTGATGCTTATCTGTGCGATGGGGTGTAACGATCCCTTACCACGACAGACGCTGCAACGCCGCACCATATCCCTTAGTCCCATGTTCTAGTTCCCGCCAGTACAAGGCAATTCATATGACAAGATGGACTTTGCCCCGGTAGGGACGTTGGACTCCCACCAGATCCTCGCTATCCTATGCTATTCCTGTAAACACATGGTGCCATATTCAGGCGTGCGCGGGGATCGATAAACCTAACTCCACGATCGTTCTTCGGACTATCTTACCCAGGGAAAAATAGAGGCATCTTTCCAGCAATAAACCGAATTCGCCGTTCTTATATAGGAGTCCGAACGTGTTGGGATTCTGTTTCGCCCTGTCCTATCGTGCGATATCTAAGAAAACCCCTCACTGCAAGTAAAAGATTGTTGGAAAGATTGATGGCGCATGACTGGCAGGACAATAGAGCCCCCATGGGAACCATGGAGATGATGAGAGCGTCCTGAGAATGATTACCGCGACAATTCCGAGTTTAAGGGCCGCCCAGCATTATATTGTCAGCCGAGTCTGGTGTGTGAACAGCCCGAACACTGGGGCCGAGGGAACCTGCAACCTTTAAAATGTAAAAAATGAGGCGCCATGTAGATGGCGTTGGACTAATTATTCCGATCGGAAAAACTCCTAAAGAGGGCTCGAATCTTGTGTGGGGGGGCGGCCTTAATAACATCGGTGGTCAACGTCAAGTACGCGGCACCTATTGCAATGTCAAGCTATATTATCTACCTTGACTGAAAGACACCCTATAAATGGCCAAACAATCCACGACAACAGTTCACTAGGTGATGGATAACCCTGTGTACCAGCCCTCTTGTCGGTAGTAGAGCGGGAAAGCTGTGATGCTTATCTGTGCGATGGGGTGTAACGATCCCTTACCACGACAGACGCTGCAACGCCGCACCATATCCCTTAGTCCCATGTTCTAGTTCCCGCCAGTACAAGGCAATTCATATGACAAGATGGACTTTGCCCCGGTAGGGACGTTGGACTCCCACCAGATCCTCGCTATCCTATGCTATTCCTGTAAACACATGGTGCCATATTCAGGCGTGC'

# we need 4 variables to count every specific nucleotide
a, c, g, t = 0, 0, 0, 0

# somehow we have to go over every character in the DNA string & count which letter we encounter

for nucleo in dna_string: # C inside the nucleo variable
    if nucleo == 'A': 
        a += 1
    elif nucleo == 'C': 
        c += 1
    elif nucleo == 'G':
        g += 1
    elif nucleo == 'T':
        t += 1
    else:
        print('DNA string contains errors')


# calculate the GC percentage
try:
    cg_perc = ( (c+g) / (a+c+g+t) )
except(ZeroDivisionError):
    print("Haven't you paid attention in math class, you can't divide by zero")
    cg_perc = 0
    
# print our counter variabels  the %
print(a,c,g,t)
print(cg_perc)