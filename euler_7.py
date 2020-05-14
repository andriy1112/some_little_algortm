list = []
for i in range(1,True):
    point = 0
    for j in range(1, i):
        if i % j == 0:
            point += 1
    if point < 3:
        list.append(i)
        print(list(i))
    if len(list) == 1001:
        break

