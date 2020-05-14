import sys

sys.stdin = open('aplusb.in','r')
sys.stdout = open('aplusb.out','w')
a, b = map(int, input().split())
print(a + b)
