import math


hate_levle = 0
n = int(input())

A = []
B = []
C = []

pA = 0
pB = 0
pC = 0

for i in range(n):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)

    A.append(a)
    B.append(b)
    C.append(c)

for j in A:
    pA += j

pA = int(pA / len(A))

for l in B:
    pB += l

pB = int(pB / len(B))

for k in C:
    pC += k

pC = int(pC / len(C))

for i in range(n):
    hate_levle += math.fabs(pA - A[i]) + math.fabs(pB - B[i]) + math.fabs(pC - C[i])

print(int(hate_levle))