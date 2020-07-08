# This program searches the uniprot website for a specific protein and then determines if it the protein has a 
# N-glycosylation motif and returns the name of the protein and the location of the motif
import urllib3
import re

http = urllib3.PoolManager()
large_dataset = open('rosalind_mprt.txt')
protein = large_dataset.readlines()

for i in protein:
    name = i.strip('\n')
    url = 'https://www.uniprot.org/uniprot/' + name + '.fasta'
    response = http.request('GET', url)
    r = response.data.decode("utf-8")
    start = re.split('SV=.',r)
    seq = start[1]
    seq = seq.replace('\n','')
    regex = re.compile(r'N(?=[^P][ST][^P])')
    index = 0
    out = []

    while(index<len(seq)):
        index += 1

        if re.search(regex,seq[index:])  ==  None:
            break

        if re.match(regex,seq[index:]) != None:
            out.append(index + 1)
    
    if out != []:
        print (name)
        print (' '.join([str(i) for i in out]))
