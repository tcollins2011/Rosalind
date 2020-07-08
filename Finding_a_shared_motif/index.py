data = open('data_set.txt').read()

# Separates fasta file to a list of DNA strings
def clean_data(fasta):
    cleaned = []
    data_set = fasta.strip().split('>')   
    for dna in data_set:
        if len(dna):
            i = dna.split()
            target = ''.join(i[1:])
            cleaned.append(target)
    return cleaned

def find_Longest(lst,shortStr):
    n = len(lst)
    s = shortest
    l =  len(s)  

    response = ['']

    for i in range(l):
        # for i in range 0,14 
        for j in range ( i + 1, l + 1):
            # for j in range (whatever i is + 1 to 15)
            # make a substring that is equal to index it to j of the word s
            substring = s[i:j] 
            k = 1 
            for k in range(n):
                # for every string in the list
                # check if the previously defined substring is in the word
                # as soon as its not break
                if substring not in lst[k]:
                    break
            # if the substring was in everyword of the list then check to see if it is longer than response
            # if it is it empties the list add the new string
            if (k + 1 == n and len(response[0]) < len(substring)):
                response = []
                response.append(substring)
            # if the substring is the same length as the first index of the list it appends the new substring
            elif (k + 1 == n and len(response[0]) == len(substring)):
                response.append(substring)
    return response


if __name__ == "__main__": 
    clean_DNA = (clean_data(data))
    shortest = clean_DNA[0]
    for i in range(len(clean_DNA)):
        if (len(clean_DNA[i]) < len(shortest)):
            shortest = clean_DNA[i]
    print (find_Longest(clean_DNA,shortest))
