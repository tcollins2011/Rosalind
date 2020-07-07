# Need to get list of sucession numbers
#search for hte webpage with the sucession number
# Determine if it has the motiff
# ouput name of protein
# output the locations of the motiff

import urllib3
import re

proteins = ['A2Z669', 'B5ZC00', 'P07204_TRBM_HUMAN', 'P20840_SAG1_YEAST']


for i in proteins:
    name = i.strip('\n')
    url = 'https://www.uniprot.org/uniprot/' + name + '.fasta'
    print (url)