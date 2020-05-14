n = input()
n = int(n)
x = []
copy = []
point = 0
for i in range(n):
    point = int(input())
    x.append(point)
    copy.append(point)
x.sort()
z = x[1] - x[0]
print(z)

f_num = x[1]
s_num = x[0]
print(copy.index(f_num) + 1, copy.index(s_num) + 1)
