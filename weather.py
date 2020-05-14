n = int(input())
a = list(input().split())
for i in range(len(a)):
    a[i] = int(a[i])

for j in a:
    if j > 0:
        print(a.index(j)+1, end=' ')
