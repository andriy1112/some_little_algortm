import sys
sys.stdin = open('lesson.in', 'r')
sys.stdout = open('lesson.out', 'w')
i = input()
a, b, c, d = map(int, i.split())
n1 = a*(b+c-d)
n2 = c*(a+d-b)
n3 = d*(c+b-a)
n4 = b*(d+a-c)
list_all_nums = [n1, n2, n3, n4]
if max(list_all_nums) == n1:
    print('0')
elif max(list_all_nums) == n2:
    print('1')
elif max(list_all_nums) == n3:
    print('2')
else:
    print('3')
