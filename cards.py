from collections import Counter


n = int(input())
card = list(input().split())
same = []

same = [k for k, v in Counter(card).items() if v > 1]

stroka = ''

for s in same:
	stroka += s

result = list(set(card) - set(same))

if len(result) > 0:
	stroka += result[0]

for t in same[::-1]:
	stroka += t
	
print(stroka)
