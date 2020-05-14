with open('class.in', 'r') as inp:
    with open ('class.out', 'w') as outs:
        f_line = inp.readline()
        for i in range(int(f_line)):
            a, b = list(map(int, inp.readline().split()))
            a, b = int(a), int(b)
            if (a*b) % 2 != 0:
                outs.write('HI\n')
            else:
                outs.write('TAK\n')

