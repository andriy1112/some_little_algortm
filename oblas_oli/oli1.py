import math


x1, y1, r1 = input().split()
x1, y1, r1 = int(x1), int(y1), int(r1)
x2, y2, r2 = input().split()
x2, y2, r2 = int(x2), int(y2), int(r2)

distance = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

f1 = 2 * math.acos(((r1*r1) - (r2*r2) + (distance*distance)) / (2 * r1 * distance))
f2 = 2 * math.acos((r2*r2 - r1*r1 + distance*distance) / (2 * r2 * distance))
s1 = ((r1*r1) * (f1 - math.sin(f1))) / 2
s2 = ((r2*r2) * (f2 - math.sin(f2))) / 2

result = s1 +s2
print(result)