a = 2
b = 2
c = 2
d = 2
k = 0
sum = 0
list = [a,b,c,d]

def flow(a,b,k):
    if a > 0 and b > 0:
        if a < b:
            pass
        elif a > b:
            k += a - b
    else:
        if a == 0 and b == 0:
            pass
        elif a > 0 and b == 0:
            k += a
        elif a == 0 and b>0:
            pass
    return k

print(flow(list[0], list[1], k) + flow(list[1], list[2], k) + flow(list[2], list[3], k+list[3]))