point = 10
i = 1
while True:
    if point % i == 0:
        i += 1
    else:
        i = 1
        point += 10
    if i == 20:
        break
print(point)

