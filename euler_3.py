list = []
numb = 13195
for i in range(1, numb):
    if numb % i == 0:
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count < 2:
            list.append(i)

for i in list:
    print(i)