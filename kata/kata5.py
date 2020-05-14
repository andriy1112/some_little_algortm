cslist = []
rez_list = []


def c(x, y):
    point = 0
    coordinates_list = []
    for i in range(1, x+1):
        for j in range(1, y + 1):
            coordinates_list.append([i, j])

    for k in coordinates_list:
        if [x + 1, y] in coordinates_list or [x, y + 1] in coordinates_list \
                or [x - 1, y] in coordinates_list or [x, y-1] in coordinates_list:
            point += 1

    if point == x * y:
        rez_list.append('TAK')
    else:
        rez_list.append('HI')


with open('class_in.txt') as cl:
    lines = cl.read()
    lines_xy = list(lines)
    count_test = int(lines_xy[0])
    for p in range(int(lines_xy[0])):
        lines_xy.remove('\n')
        lines_xy.remove(' ')
    for r in range(1, len(lines_xy)):
        cslist.append(int(lines_xy[r]))
    for o in range(0, count_test+2, 2):
        c(cslist[o], cslist[o+1])


with open('class_out.txt', 'w') as outs:
    for n in rez_list:
        outs.write(n)
        outs.write('\n')
