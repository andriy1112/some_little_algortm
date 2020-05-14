rez_1 = 0
now = 0
rez_2 = 0
for i in range(101):
    rez_1 +=  i*i
    now += i
    rez_2 = now * now
print(rez_2 - rez_1 , 'разность между суммой квадратов и квадратом суммы первых ста натуральных чисел')