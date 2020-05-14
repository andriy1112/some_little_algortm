abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
s = 'ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ'
s = s.lower()
point = 0
for i in abc:
    if i in s:
        point += 1

if point == len(abc):
    print('true', point)
else:
    print('false', point)