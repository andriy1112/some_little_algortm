point = 0
goal_list = []
with open('football.in', 'r') as inps:
    number = int(inps.readline())

while True:
    if sum(goal_list) == number:
        with open ('football.out', 'w') as outs:
            outs.write(str(point))
            break
    elif sum(goal_list) > number:
        with open('football.out', 'w') as outs:
            outs.write('-1')
            break
    point += 1
    goal_list.append(point)
