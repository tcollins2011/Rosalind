
# Cleans the fasta file by combing the identifying line of the fasta file with the sequence info in a list
def clean_fasta(fasta):
    results = []
    data = fasta.strip().split('>')

    for dna in data:
        if len(dna):
            i = dna.split()
            first = i[0]
            rest = ''.join(i[1:])
            results.append((first, rest))
    return results

#  Loops through the cleaned fast a file and looks for an overlap in the final n nucleotides of one string and the first n nucleotides of another
def overlap_graph(fasta, n):
    results = []

    dna = clean_fasta(fasta)

    for k1, v1 in dna:
        for k2, v2 in dna:
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1, k2))
    
    return results


#imports a data set of fasta DNA sequences if this the main module and then then runs overlapgraph graph for every entry
# Returns the fasta line identifier for sequences that overlap
if __name__ == "__main__":

    large_dataset = open('data_set.txt').read()

    for edge in overlap_graph(large_dataset, 3):
        print (edge[0], edge[1])