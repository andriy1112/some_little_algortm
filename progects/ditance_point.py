import math

list_a = [[-1, 3], [6, 2], [0, 1], [-2, 2]]
list_b = list_a.copy()
smalest = []
AB_min = 100
AB = 0
point = 0
for i in range(len(list_a)):
    for j in range(len(list_b)):
        x = list_a[i][point], list_b[j][point]
        y = list_a[i][point+1], list_b[j][point+1]
        if x == (list_a[0][0], list_b[0][0]) and y == (list_a[0][1], list_b[0][1]) or x == (list_a[len(list_a)-1][0],\
            list_b[len(list_b)-1][0]) and y == (list_a[len(list_a)-1][1], list_b[len(list_b)-1][1]) or x[0] == x[1] and y[0] == y[1]:
            pass
        else:
            AB = math.sqrt(pow(x[1] - x[0], 2) + pow(y[1] - y[0], 2))
            AB = math.fabs(AB)
            if AB_min > AB:
                AB_min = AB
                smalest.clear()
                smalest.append(x)
                smalest.append(y)
print(AB_min)
print('x:', smalest[0])
print('y:', smalest[1])