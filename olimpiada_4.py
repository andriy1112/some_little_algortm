A = 3
B = 3
C = 3
point = 0

for i in range(max(A, B, C)):

    if A <= 0 :
        break
    A -= 1
    point += 1

    if B == 0:
        break
    B -= 1
    point += 1

    if C == 0:
        break
    C -= 1
    point += 1

    if B == 0:
        break
    B -= 1
    point += 1

print(point)

