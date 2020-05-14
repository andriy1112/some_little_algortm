import sys
point = 0
goal_list = []
sys.stdin = open('football.in', 'r')
sys.stdout = open('football.out', 'w')
number = int(input())
for i in range(8000):
    if sum(goal_list) == number:
        print(point)
        break
    elif sum(goal_list) > number:
        print(-1)
        break
    point += 1
    goal_list.append(point)
