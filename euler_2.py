firstFibo = 1
secondFibo = 2
nextFibo = 0
suma = 0
for i in range(0 ,4000000):
    nextFibo = firstFibo + secondFibo
    if firstFibo > secondFibo:
        secondFibo= nextFibo
    else:
        firstFibo = nextFibo
    if nextFibo % 2 == 0:
        suma =+ nextFibo
    if nextFibo >= 4000000:
        break
print(suma)