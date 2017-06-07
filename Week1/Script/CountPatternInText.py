"""Author: Laura Gutierrez Funderburk
Date: June 2017"""

# coding: utf-8

# In[83]:

def PatternCount(text,pattern):
    count = 0
    for i in range(len(text)):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count


# In[92]:

test = PatternCount("GATGTTCGATAAATGTTTCGATAACATACTCTGTTCGATACGTTCTTTTCGATATTCGATATAGTTCGATAATTTTCGATAGTTCGATATTCGATAGTCTAATTCGATATTCGATATTTCGATATTCGATAGTTTTCGATAGTTCTGTTCGATAGGTTCATTCGATATAGCCGGAGTTTCGATACTCGTTCGATATTCGATATTTCGATAGCCTTCGATACTTCGATAAAGCCTATTCGATAGGGATGAGAGCTTCGATACGAGTCCTTCGATAGCCCTACAGTTCGATATTCGATACTTTCGATATTTCGATACATTCGATATTCGATATTCGATAAAGGTTTTCGATATTCGATATTCGATAAGAACCTTATATTCGATAAATTCGATATTCGATATTCGATATTCGATATTCGATATATTTCGATATTCGATACTTCGATATTCGATATTTCGATATTCGATAAGTTCGATAGTTCGATATTCGATATTCGATAAGTTCGATATTTCGATATTCGATAATTCGATATCTTCGATATTCGATATTCGATATTCGATAGATCTTCGATATTCGATACTTGGATTCGATACTTCGATAGTATATTTCGATATTCGATATGTAGAACCCTCGGTTCGATACGAACGGTGGCCTTCGATACGTGGCGTTCGATATTCGATATTTCGATACTTCGATATTCGATACTGCTTCGATACTGGTTCGATAAATTCGATAAGCATTCGATATTCGATATTCGATAAGCTTCGATAGTTCGATACTTCGATATAGTTCGATATCCCGCGTTCGATATTCGATACAACTTCGATAGTTCGATACTTCGATAGATTCGATAATTTCGATACCTTCGATAGCGCATTCGATAATTCGATATTCGATATTCGATAATTCGATATTCGATACTTCGATAGATTCGATATTTCGATATTCGATATTTCGATAATTCGATAGTTCGATATTCGATAACGTTTTCGATACCTCTTAACGTTCGATAGAAGGCATGTTCGATATTCGATATTCGATATTCGATAGTTCGATA","TTCGATATT")
print(test)


# Code Challenge: Solve the Pattern Matching Problem:
#      Input: Two strings, Pattern and Genome.
#      Output: A collection of space-separated integers specifying all starting positions where Pattern appears
#      as a substring of Genome.

# In[7]:

def PatternMatching(Pattern,Genome):
    positions = []
    for i in range(len(Genome)):
        if Genome[i:i+len(Pattern)] == Pattern:
            print i
            positions.append(i)
    return positions


# In[14]:

print(PatternMatching("TCCCTAGTC","TTGTCCCTAGTGTCCCTAGTCCCTAGATCCCTAGCGTCCCTAGAGGTACGCTCCTGTTCCCTAGTACGTCCCTAGTTGATTTCCCTAGAATCCCTAGTCCCTAGCTCCCTAGCTCCTTCCCTAGGTCCCTAGATTCCCTAGAATCCCTAGTGCCGCTCCCTAGCGTCCCTAGCATCCCTAGCTCCCTAGTCCCTAGTGAGGCTGTTGGTTCCCTAGGTGTCAAGTGGATCCCTAGTCGTCCCTAGATAATCGAAGCCGTTCCCTAGCTCCCTAGCTCCCTAGACTCCTGAGCAGTCCCTAGCTCCCTAGTCCCTAGCTAGACTAGCTAGTTTCCCTAGTCCCTAGTAATCCCTAGGCTCCCTAGAGACCTGTTTTCCCTAGGACTTCCCTAGAGACTCCCTAGTCCCTAGGCTTCCCTAGTCCCTAGTCCCTAGTAATAGCTCCCTAGTCCCTAGAATCCCTAGCATCCTCCCTAGTCCCTAGATCCCTAGCTCCCTAGTCCCTAGGGGTCCCTAGCTCCCTAGATTCATTCCCTAGAACGCTCCCTAGTTCCCTAGCTCCCTAGGTCCCTAGAGCAGGGTATCCCTAGGGTGTCCCTAGCCCAAATTTTCCCTAGGTCCCTAGCGTCCCTAGGGTCCCTAGAGGCATATTCCCTAGACTCCCTAGTCCCTAGCGCTTCATCCCTAGCACCTCCCTAGTCCCTAGTCCCTAGATATCCCTAGTCCCTAGCGTCCCTAGCGTGTCCCTAGCTAATCCCTAGGCTCCCTAGTCCCTAGCTCCCTAGAGGGTCCCTAGCTTTCCGTCCCTAGCTTCCCTAGCGATCCCTAGTTCCCTAGTCCCTAGTCCCTAGATCCCTAGTCCCTAGGAGTTTCCCTAGTCCCTAGGTCCCTAGGTAGTCCCTAGTCCCTAGCGTCCCTAGAAATCCCTAGTTCCCTAGGCTCCCTAGATCCCTAGATCCCTAGTGTCCCTAGCCCTCCCTAGCCTCCCTAGGATCCCTAGCCGATTTTTCTCCCTAGTTCCCTAGTCCCTAGGTTCCCTAGTCCCTAGAGCAGCGTTCCCTAGGGCTTCATCCCTAGCTCCCTAGTCCCTAGGAGTATTCCCTAGTCCCTAGCATCAGCATCCCTAGGTCGTCCCTAGGTCCCTAGTACCTCTCCTTCCCTAGTCATCCCTAGCGTCCCTAGTCCGGTCCCTAGGTCCCTAGCTCTCCCTAGAGTCCCTAGATCCCTAGTCCCTAGGAGGGGTTCCCTAGTGTCCCTAGTCCCTAGCATAGTCCCTAGTCTAGTTCCCTAGTCCCTAGCGTATCCCTAGGGGCTCCCTAGAGATCCCTAGTCCCTAGAAGTTCCCTAGCCTTCCCTAGAGTCCCTAGGATTCCCTAGTCCCTAGGTGTCCCTAGGTCCCTAGTCCCTAGTGGACCTCCCTAGGTATTTACCTCCCTAGACGCTCCCTAGGTTCCCTAGACGTCTTCCCTAGAGATCCCTAGTCAGTCCCTAGTTCCCTAGATTCCCTAGTTCATCCCTAGCCTCCCTAGGTATCCCTAGAAAGTTCCCTAGGCCATCCCTAGCCTCCGTCTCCCTAGTTAGACGTCCCTAGAGCTCCCTAGCTCCGCACTCCCTAGCAAGTCCCTAGATCCCTAGCTTCCCTAGGATTGATGGTCCCTAGGCCGTCCCTAGAAGTCCCTAGGTCTTCCCTAGTCCCTAGTCCCTAGGTCCCTAGGCAGTTATCCCTAGGTGAGTCCCTAGGCCGTGGTCCCTAGTCCCTAGTCCCTAGATCCCTAGAGTCTGCAGCGCGGCCCAACCTCCCTAGCACTCCCTAGAGTCCCTAGTCCCTAGCTATCCCTAGTCCCTAGTCCCTAGGTCCCTAGTTTGATCCCTAGTCCCTAGTCCCTAGTCCCTAGCTTTCCCTAGCAGTCCCTAGCCGTCTGCGTCCCTAGGGGTCCCTAGTCCCTAGTACTCCCTAGCGTCCCTAGCACGTTTAATCCCTAGTCTCCCTAGGTCCCTAGCTCCCTAGCCGTCCCTAGTCCCTAGCCTGTCCCTAGTCCCTAGTTCCCTAGTCCCTAGGTCCCTAGCTCCCTAGAGAGTCCCTAGATCCCTAGATCCCTAGTTCCCTAGTCCCTAGGGGATCCCTAGAAGTCCCTAGGTCCCTAGGTCCCTAGTGTTCCCTAGGGATCCCTAGCGTGGTGTCCCTAGAATCCCTAGTTCCCTAGAGTCCCTAGCTTCCCTAGATCCCTAGCTCCCTAGATCCCTAGATCCCTAGTCCCTAGCGATCCCTAGTCCCTAGTCCCTAGTGGCAGTTCCCTAGATTCCCTAGTACGGTCCCTAGCTCCCTAGTGATCCCTAGTTATATCCCTAGACCCTGAGCATCCCTAGTCCCTAGCCGGTCCCTAGTCCCTAGTCCCTAGTATCCCTAGATACAGACCTCCCTAGCAACGAACGATCCCTAGGAACTCCCTAGCCTATTCCCTAGTTCCCTAGTCCCTAGTCCCTAGAAATTATCCCTAGTCCCTAGTATCCCTAGGATCCCTAGTTCCCTAGAGCGATCCCTAGATCCCTAGGTCCCTAGTCCCTAGCTCCCTAGCTGGCTCCCTAGTCCCTAGTCTCCCTAGCCTCCCTAGGTCCCTAGCATCCCTAGTCCCTAGGGATCCCTAGTCCCTAGTCCCTAGCATCCCTAGTCCCTAGTATCCCTAGGTCCCTAGTCCCTAGGGTCCCTAGATTATCCCTAGAACTCCCTAGGTGCTCCCTAGATCCCTAGGTGTCCCTAGATCCCTAGGGTCTCCCTAGACATCCCTAGTGGTATCCCTAGATTGTTCCCTAGTCCCTAGAAATCCCTAGGCATCCCTAGTGCTCCCTAGTCCCTAGCGGTCTAGGTGTCCCTAGATTCCCTAGGTCCCTAGATGTCCCTAGTCCCTAGTATCCTTGTGGATCCTCGTTCCCTAGACACTGCTCCCTAGCTGGCGCAGTTCCCTAGTGTCCTCCCTAGTCCCTAGCTTCCCTAGGTCCCTAGTCCCTAGATCCCTAGTTCCCTAGCTCCCTAGTTCCCTAGGTCCCTAGATCCCTAGTCCCTAGTTTCCCTAGCATTCCCTAGTATTCCCTAGCGCTCCCTAGTTCCCTAGATCCCTAGTCCCTAGTCCCTAGCCGGGCTGCGTTCCCTAGTCCCTAGCCTCCCTAGCGACTTCCCTAGATCCCTAGTCCCTAGTCCCTAGGACCCCTCCCTAGAAATTCCCTAGTCCCTAGTCCCTAGTTCCCTAGCTCTCGTACATTTTCCCTAGTCCCTAGTCCCTAGAGGCATAATCCCTAGTCCCTAGTCCCTAGGAATCCCTAGTTCCCTAGGTCCCTAGCATGCATCCCTAGGATTCCCTAGTCCCTAGATCCTCCCTAGGTCCCTAGTCCCTAGGTCCCTAGGTTTGCGTCCCTAGTCCTAGAATCCCTAGTCCCTAGTCCCTAGTCCCTAGTTCCCTAGATCCCTAGTAAATCCCTAGATCCCTAGGGTCTTCCCTAGTTCCCTAGATTCCCTAGCGTCCCTAGGATCCCTAGACCTCCCTAGAGCAGGCTCGCCTTTCCCTAGTCCCTAGATCCCTAGGCATATTCCCTAGTCGGTCCCTAGGATCTGGCTGCAATACTCCCTAGAATTCCCTAGTCCCTAGTCCCTAGGGACGATCCCTAGGATTTCCCTAGTCCCTAGGTCCCTAGGTATTTTCTCACTCCCTAGTCCCTAGCATCCCTAGTCCCTAGCATCCCTAGAGAAGCATCTCGAAGTCCCTAGGTTCCCTAGTCCCTAGGGTTGAGGTCCCTAGGTTCCCTAGCTATTCCCTAGGCTCCCTAGTGATTCCCTAGTCCCTAGCGGAATTCCCTAGTCCCTAGAGTCCCTAGTCCCTAGTCCCTAGGACCTCCCTAGTCCCTAGCAGTTTCCCTAGTTCCCTAGAACCTTCCCTAGGTCCCTAGATCCCTAGTCCCTAGGCATTGATGCGTTCCCTAGTCCCTAGTCCCTAGCTGTCCCTAGATCTTCCCTAGGTCCCTAGAGAGGGCCTCCCTAGAAGTCTTCCCTAGACTCCCTAGATTTTCCCTAGCACTCCCTAGTCCCTAGCCCTCCCTAGTCCCTAGTCCCTAGATTCCCTAGGTCCCTAGACACGTCCCTAGATCCCTAGACTCCCTAGCTCCCTAGCATTCCCTAGTGTCCCTAGTTTTTCCCTAGCCGTTCCCTAGTCCCTAGGGACTCCCTAGTCCCTAGTACATCCCTAGCTTTCCCTAGATCCCTAGGAGTCCCTAGACCTCCCTAGACCTCCCTAGTTCCCTAGTGTTCCCTAGTCCCTAGTCCCTAGCTCCCTAGGTCCCTAGTTCCCTAGTGCACTTCCCTAGTCCCTAGTCCCTAGTCCCTAGTCCCTAGGATTACCCAATCCCTAGGGCTCCCTAGTTTATCCCTAGTCCGTCCCTAGGATGATCCCTAGAGTTGACGTCCCTAGTCCCTAGTCCCTAGCTTTCCCTAGTTCCCTAGCGAATGCTACCTCTCCCTAGAATCCCTAGTCAATAATCCCTAGATCTTCCCTAGCCGTTTCCCTAGTTCCCTAGGTGATCCCTAGGTTCCCTAGATCCCTAGTTTCCCTAGTGGTCCCTAGTCCCTAGGGGGGTCCCTAGCAAGACTACCTTCCCTAGGATCTCCCTAGTCCCTAGGTATCCCTAGCTGTCATCGTCACATCCCTAGACCTCCCTAGTCCCTAGACTCCCTAGTTCCTGCTTTGACTCCCTAGATTCCCTAGCTCTCCCTAGTCCCTAGACTCCCTAGGTTAACAGCTCCCTAGTCGGAACCAAATGTCCCTAGCGTCCCTAGTCCCTAGTTGTCCCTAGTCCCTAGACTTCCCTAGTGACAATCCCTAGTCCCTAGTCCCTAGTGTCCCTAGATCCCTAGCCCATCTCCCTAGTTGTTCGGGAAATTCCCTAGTCCCTAGGGCGCGTTCCCTAGTAGTCACGTCCCTAGCATTTCCCTAGTATTCCCTAGCATCCCTAGATCCCTAGCTCCCTAGTCCCTAGTCCCTAGGTCTTCCCTAGTGTCTCATGGTTCCCTAGTAGTCCCTAGGGTTTCTGGGCGGGATGTCCCTAGTCCCTAGGCCTCCCTAGTCCCTAGTCTCCCTAGTCCCTAGTCCCTAGTCCCTAGTTCCCTAGTGATCCCTAGCATCCCTAGTCCCTAGTCCCTAGTCCCTAGGTGTCCCTAGTCCCTAGTCCCTAGTCCCTAGCCATGGTTTTAAATCCCTAGATCCCTAGCTCCCTAGGATATCCCTAGGATCCCTAGTCCCTAGTCCCTAGCCACTCCCTAGGTATCCCTAGATCCCTAGTCCCTAGAAGCTCCCTAGATCCCTAGTCTTCCCTAGTCCCTAGCCTCCCTAGCTCCCTAGAAATCCCTAGTCATCAGCGTCCCTAGATCCCTAGATCCCTAGTATCCCTAGTCCCTAGTCCCTAGTCCCTAGTGCTACTCCCTAGTGGTCCCTAGTTCCCTAGACTATCCCTAGTCCCTAGCAATCCCTAGTCCCTAGGGTCCCTAGGTCCCTAGTCCCTAGTTGAACTCCCTAGTCCCTAGTTCCCTAGGTCCCTAGGTGTCCCTAGTATCTTCCCTAGTGTGGTCAGAAATCCCTAGCCTCCCTAGGTCCCTAGGTCCCTAGCTCCCTAGCGTCCCTAGCGTCCCTAGTTTCCCTAGCTCCCTAGAATCCCTAGCGATCGTCCCTAGTCCCTAGTCCCTAGTCCCTAGGCCGTCCCTAGTGGACTCCCTAGTCCCTAGTCCCTAGTTCCCTAGTGTAACTCCCTAGTCCCTAGTCCCTAGGCTCCCTAGTCCCTAGATAGTTTTATATCCCTAGGTCCCTAGACGTGTGGTCCCTAGGTATCCCTAGTCCCTAGTCCCTAGTCCCTAGGGCTCCCTAGTCCCTAGTCCCTAGTTCCCTAGGCCTCCCTAGTCCCTAGTTCCCTAGGATGACCTCCCTAGCTTCCCTAGTTTCCCTAGTACTAGCTTCTCCCTAGTCCCTAGTCCCTAGCGACCGTCCCTAGCCTCCCTAGTCCCTAGGTTATTTCCCTAGAAGCACCTCCCTAGAGTCCCTAGCTCCCTAGAGTCCCTAGTCCCTAGTGCTCCCTAGCTCCGTCGTCCCTAGTCCCTAGTTCATCCCTAGTTCCCTAGGGATTTCCCTAGGGTTAGTTCGGGATCCCTAGATGTCCCTAGAGTCCCTAGTACCACCTCCCTAGTCACTCCCTAGATTCCCTAGGATTTTTGCATCCCTAGTCCCTAGTCCCTAGTGTCCCTAGTTCCCTAGTCCCTAGTTCCCTAGTCCCTAGATCCCTAGATCCCTAGCTCCCTAGTCCCTAGATCCCTAGCGTTACGTCTTTGTTCCCTAGAGTCCCTAGGTCCCTAGCCAGTCCCTAGTCCCTAGTCTGCTCCCTAGTCCCTAGGCGCCTCCCTAGAACGTTAGTCCCTAGCCTCATGCGACGCGTCCCTAGCCCTCCTCCCTAGGCATCTGTGTTCCCTAGTATCCCTAGGGCTGGTCCCTAGTGTCCCTAGCTTTCCCTAGCGTCCCTAGCTCAGATCTGCCCGCGATCCCTAGCTCCCTAGCCTCCCTAGGTGAAGATTTCACCTTCCCTAGTTCCCTAGTTCCCTAGTCTCCCTAGGGACCAAGATCCCTAGGAAGCACGGATCCCTAGTCCCTAGATTTGTCCCTAGGTCCCTAGTCCCTAGTCCCTAGCTCCCTAGTATTTCCCTAGTACTACTCCCTAGGGCTCCCTAGCTAGTTCCCTAGCGTGTTCAGCCCGTCCCTAGACCATCCCTAGGTGTCCTCCCTAGCTAAATGTCTCCCTAGCCTGCTGTCCCTAGATCCCTAGGCCCGGTGTTCAAATCCCTAGACATCTCCCTAGTCCCTAGAACTCCCTAGGTCCCTAGATCCCTAGTCCCTAGTCCCTAGCCTCCCTAGTATCGGGCTGTAAGATCCCTAGCTCCCTAGACTCCCTAGATCCCTAGATCCCTAGGGTCCCCTCCCTAGGATCCCTAGTCCCTAGTCCCTAGTCCCTAGGTTTTCCCTAGGTCCCTAGAGTCCCTAGGATCCCTAGCTCCCTAGGGTAGTCCCTAGCCCTCCCTAGTCCCTAGGGTCCCTAGTCCCTAGACATTCTCCCTAGTTCCCTAGTCCCTAGGTGTCCCTAGGGCATCCCTAGTTATCCCTAGGGTCCCTAGTCCTCAACCAAACGGTCCCTAGTCCCTAGATGTGAAACACGTGTAATCCCTAGCGTTGTCCCTAGCGGTCCCTAGGTCCCTAGATCCCTAGGGTCCTCCCTAGTCCCTAGTTCCCTAGAAGGATCCCTAGTATTACGATCCCTAGTCCCTAGAAGCTTCCCTAGCTCCCTAGTCCCTAGGTCCCTAGTCCCTAGTCCCTAGATACGCTCTCCCTAGTCCCTAGTTCCCTAGTCCCTAGTCCCTAGTTCCCTAGATTCCCTAGCATTCCCTAGCATCCCTAGTCCCTAGTGGGTACTGGTCCCTAGGGTCCCTAGTCCCTAGTCCCTAGTTGTCCCTAGTCCCTAGTCCCTAGAGTCCCTAGCTTCCCTAGCTCCCTAGCTCACTCCCTAGTCCCTAGGTCCCTAGTCCCTAGTCCCTAGTCCCTAGGTCCCTAGATGAGGTCCCTAGCGCTCCCTAGATCCTCCCTAGTCCCTAGATCCCTAGGCTCCCTAGCTCCCTAGCTCCGCCTCCCTAGGTCCCTAGATTCCCTAGTCCCTAGTCCCTAGATCCCTAGTCCCTAGTCCCTAGTCCCTAGCAATTGTGCGTCCCTAGGATAGGGTCCCTAGACGGGTCCCTAGACTTCCCTAGATCCCTAGCAATCCCTAGTCCCTAGATGACTCCCTAGAATCCCTAGTGTCCCTAGTCCCTAGTCCCTAGTCCCTAGGCATCCCTAGCCCTACCTCCCTAGTTCCCTAGAATAACTTCCCTAGATATTTATCCCTAGATGTTTCCCTAGTCCCTAGAACTTGTTCTGTCCCTAGCATCCCTAGGTTCCCTAGGCTCCCTAGATCCCTAGCCGTTCCCTAGTCCCTAGTCCCTAGAGCCAGCCCTCCCTAGTCCCTAGTCCCTAGGTGTCCCTAGTCGGCACTGACGTTCCCTAGCTCCCTAGTCCCTAGTTCCCTAGTCCCTAGTCCCTAGTTCCCTAGCATCCCTAGTCCCTAGTCCCTAGCCTCCCTAGGTCCTCCCTAGAATCCCTAGGACTCCCTAGGTGGTCCCTAGTCCCTAGTCCCTAGGACAGAACTCCCTAGTTCCCTAGTCCCTAGTCCCTAGATCCCTAGTCCCTAGTATGCAGTCCCTAGTATACGTCCCTAGAGACTCCCTAGTCCCTAGTCCCTAGAACGTATGTGCAAGACGTCTAATCCCTAGTCCCTAGTTCCCTAGCTCCCTAGACAGAGCATCCCTAGGAGTCATCTCCCTAGTCCCTAGGGCGTTCCCTAGATCCCTAGTCCCTAGTACTCCCTAGAGCCCACATTATGTCCCTAGCTTATCCCTAGTCCCTAGAACCCACTCCCTAGCCCTTCCCTAGATCCCTAGTCCCTAGTAACTCCCTAGAACCTCCCTAGTATCCCTAGAAGAATACTCCCTAGTTCCCTAGATCCCTAGTCCCTAGGTCCCTAGTCCCTAGTAATATTCCCTAGGGCATCCCTAGTAATCCCTAGTCCCTAGGATCCCTAGGTAATGCATGTCCCTAGTTCCCTAGTATAGTCCCTAGCTCCCTAGTCCCTAGTCCCTAGAGTTCCCTAGTCCACGATCCCTAGTCCCTAGGCGATCCCTAGTCCCTAGATTCCCTAGTCCCTAGATCCCTAGATCCCTAGCTCCCTAGTTCCCTAGTTAGATCCCTAGCATTCCCTAGGTCCCTAGGTCCTCCCTAGTCCCTAGGTCCCTAGGTCCCTAGTCCCTAGCATCTTCCCTAGTCCCTAGCAACGTCCCTAGTCTTGCTCCCTAGGTCCCTAGTGATTCGCGCCATCCCTAGTACTCCCTAGCTCCCTAGTCCCTAGTCCCTAGCCAATCCCTAGGCTCCCTAGTCCCTAGTCCCTAGAGTTTCCCTAGATCCCTAGTCCCTAGTGAGCACAGTCCCTAGGCCACTTCCCTAGAAGGTTTCAATTCCCTAGTACTCCCTAGCCTCCCTAGTAAGTCCCTAGCCACCTCCCTAGACTAGTTATCCCTAGCCTGTGCTCCCTAGGATTCCCTAGGGTTCCCTAGTCCCTAGTCCCTAGCGTCCCTAGTCCCTAGTCGTGGGTCCCTAGGTCCCTAGACAGGTCCCTAGTAATCCCTAGCGTTCCCTAGTCCCTAGGGTCCCTAGTTCCCTAGTCCCTAGAATCCCTAGTCCCTAGTCCCTAGTCACCTTCCCTAGTCCCTAGTCCCTAGTCCGGAAGTCCCTAGTCCCTAGTCCCTAGATCCCTAGCTTGTCCCTAGCGTCCCTAGCGTCCCTAGTCCCTAGCCAGTCCCTAGCTTCCCTAGCATCCCTAGTCCCTAGGTCCCTAGCTCCCTAGATTCTTTCCCTAGCTGTCTTCCCTAGGCTTAGTTTCCCTAGATTCCCTAGTCCCTAGGTCCCTAGCATCCCTAGTCCCTAGGTCCCTAGTTGCTTTCCCTAGGTCCCTAGTTTCCCTAGTTAAGGGAGTTCCCTAGTCCCTAGAGTTCCCTAGCCTCCCTAGTCCCTAGTCCCTAGCGCTCCCTAGATCCCTAGTGTCCCTAGATCCCTAGTCCCTAGATTCGTTTGTCCCTAGGATCCCTAGTTCCCTAGTCCCTAGTTAGGCGATTCCCTAGGGCGTCCCTAGAGTCCCTAGACATCCCTAGGCCTCCCTAGTTCCCTAGCCTCCCTAGTCCCTAGTCCCTAGCTCCCTAGAAGCCTATCCCTAGATCCCTAGGTGTCCCTAGTCCCTAGGCAATCCCTAGATCCCTAGGATACGAGGATCCCTAGATCCCTAGAGG"))

