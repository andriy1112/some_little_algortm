X = 47
allX = []
pointX = []
index = 0

for i in range(1, X+1):
    if X % i == 0:
        allX.append(i)

for j in allX:
    k = j
    for l in allX:
        if k != 1 and l != 1 and k != l:
            #print(k, l)
            index += 1
        elif k == X or l == X:
            #print(k, l)
            index += 1

print(index)
