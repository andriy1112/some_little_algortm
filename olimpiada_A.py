m = 7
n = 3
point1 = 0
point2 = 0
if m > n:
    point1 = n
    point2 = (m - n) / 2
    print(point1, int(point2))
elif m < n:
    point1 = m
    point2 = (n - m) / 2
    print(point1, int(point2))
else:
    print(m, 0)