n = int(input())

if n > 10:
    ost = n % 10
else:
    ost = n

if ost == 1 and n != 11:
    print(n, 'rik')
elif ost >= 2 and ost <= 4:
    print(n, 'roki')
else:
    print(n, 'rokiv')
