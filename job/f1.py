def f1(n):
    list_s = list(str(n))
    list_num = list(map(int, list_s))
    dob = 1
    for i in list_num:
        dob *= i
    rez = (len(list_num), sum(list_num), dob)
    print(rez)


f1(24)
