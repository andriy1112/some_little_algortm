N = input()
N = int(N)
children_height = []

for i in range(N):
    children_height.append(int(input()))

player_height = int(input())

children_height.append(player_height)

children_height.sort(reverse=True)
for j in children_height:
    print(j)

print(children_height.index(player_height)+1)
