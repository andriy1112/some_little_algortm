m = 4
n = 3
for i in range(1000000):
    a = (m ** 2) - (n ** 2)
    b = 2 * m * n
    c = (m ** 2) + (n ** 2)
    if a + b + c >= 1000:
        print('yeah')
        print(a,b,c)
        break
    else:
        m += 1
        n += 1