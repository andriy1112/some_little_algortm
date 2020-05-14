def find_short(s):
    list_s = list(s.split())
    l = list_s[0]
    for i in list_s:
        if len(i) < len(l):
            l = i
    print(l)


find_short("i want to travel the world writing code one day")