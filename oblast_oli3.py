A, B, C, D = input().split()
A, B, C, D = int(A), int(B), int(C), int(D)
max = (B - A + 1) * (D - C + 1)
point = 0
N = int(input())
numbers = []

for i in range(N):
    numbers.append(int(input()))

for t in numbers:
    for k in range(A, B+1):
        for l in range(C, D+1):
            if k * l == t:
                point += 1
    if point == 0:
        print(point, '/', 1)
    elif max % point == 0:
        print(1, '/', int(max/point))
    else:
        print(point, '/', max)
    point = 0
