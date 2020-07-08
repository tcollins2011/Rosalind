# Takes in 6 numbers representing the number of couples that have the following genotypes
# Calculates the number of offspring that will dispally the dominant trait 
#AA-AA
#AA-Aa
#AA-aa
#Aa-Aa
#Aa-aa
#aa-aa   

def probabilityDominant(ratio):
    results = 2 * int(ratio[0])
    results += 2 * int(ratio[1])
    results += 2 * int(ratio[2])
    results += 1.5 * int(ratio[3]) 
    results +=  int(ratio[4]) 
    results += 0 * int(ratio[5]) 
    return results

dataset = open('rosalind_data.txt')
data = dataset.readlines()
if len(data) == 6:
    print(probabilityDominant(data))