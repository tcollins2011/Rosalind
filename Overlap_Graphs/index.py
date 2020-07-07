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


def overlap_graph(fasta, n):
    results = []

    dna = clean_fasta(fasta)

    for k1, v1 in dna:
        for k2, v2 in dna:
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1, k2))
    
    return results


if __name__ == "__main__":

    small_dataset = """
                    >Rosalind_0498
                    AAATAAA
                    >Rosalind_2391
                    AAATTTT
                    >Rosalind_2323
                    TTTTCCC
                    >Rosalind_0442
                    AAATCCC
                    >Rosalind_5013
                    GGGTGGG
                    """

    large_dataset = open('data_set.txt').read()

    for edge in overlap_graph(large_dataset, 3):
        print (edge[0], edge[1])