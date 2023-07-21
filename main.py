dna = str(input())
count = 1
string = ''
if len(dna) == 1:
    string += dna + str(count)
else:
    for i in range(0, len(dna) - 1):
        if dna[i] == dna[i + 1]:
            count += 1
        elif dna[i] != dna[i + 1]:
            string += dna[i] + str(count)
            count = 1
    for j in range(len(dna) - 1, len(dna)):
        if dna[-1] == dna[-2]:
            string += dna[j] + str(count)
        elif dna[-1] != dna[-2]:
            string += dna[j] + str(count)
            count = 1
print(string)
