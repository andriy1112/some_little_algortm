rezalt = []
num = 1112
rezultat = 0
while num != 9999:
    num += 1
    chyslo = list(map(int, str(num)))
    z = int(str(chyslo[0]) + str(chyslo[1]) + str(chyslo[2]) + str(chyslo[3]))
    sum = pow(chyslo[0], 4) + pow(chyslo[1], 4) + pow(chyslo[2], 4) + pow(chyslo[3], 4)
    if z == sum:
        print(z)
        rezalt.append(sum)

chyslo = list(map(int, str(num)))

for i in rezalt:
    rezultat += i

print(rezultat)