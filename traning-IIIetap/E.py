import sys
rezult = ''
sys.stdin = open('even-or-odd.in','r')
sys.stdout = open('even-or-odd.out','w')
input()
nums = map(int, input().split())
rez_list = []
point = 0
for i in nums:
    for j in range(1, i+1):
        if i % j == 0:
            point += 1
    rez_list.append(point)
    point = 0
for h in rez_list:
    if h % 2 == 0:
        rezult += '0'
    else:
        rezult += '1'
print(rezult)
