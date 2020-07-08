# Separates fasta file to a single DNA string
from math import factorial
def clean_data(fasta):
    cleaned = []
    data_set = fasta.strip().split('>')   
    for dna in data_set:
        if len(dna):
            i = dna.split()
            target = ''.join(i[1:])
            cleaned.append(target)
    return cleaned

# Assumes an equal number of A's and U's, as well as an equal number of C's and G's
# Can then assume that there is an au and cg  complete bipartite graph
# Then uses factorials of these complete graphs multipled together to calculate the maximum number of complete matchings
def total_matches(sequence):
    AU = 0
    GC = 0
    for nucleotide in sequence:
        if nucleotide == 'A':
            AU += 1
        elif nucleotide == 'G':
            GC += 1
    matchings = factorial(AU) * factorial(GC)
    return matchings

if __name__ == "__main__": 
    sequence = clean_data(open('data.txt').read())
    print(total_matches(str(sequence)))