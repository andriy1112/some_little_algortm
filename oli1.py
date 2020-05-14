n = input('n = ')
n = int(n)

f = input('f = ')
f = int(f)
sum = 1

for i in range(1, n+1):
    f+=i
    sum *= f

print(sum)