n = int(input())
cookies = list(map(int, input().split()))
rezult = 0
for i in cookies:
    rezult += i - 1
print(rezult)