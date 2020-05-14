number = 6830907
number = str(number)
point = 0

a = int(number[0]) * 2
b = int(number[1]) * 7
c = int(number[2]) * 6
d = int(number[3]) * 5
e = int(number[4]) * 4
j = int(number[5]) * 3
y = int(number[6]) * 2

sum = int(a) + int(b) + int(c) + int(d) + int(e) + int(j) + int(y)
point = sum % 11
if point == 0:
    print('J')
elif point == 1:
    print('A')
elif point == 2:
    print('B')
elif point == 3:
    print('C')
elif point == 4:
    print('D')
elif point == 5:
    print('E')
elif point == 6:
    print('F')
elif point == 7:
    print('G')
elif point == 8:
    print('G')
elif point == 9:
    print('H')
elif point == 10:
    print('Z')