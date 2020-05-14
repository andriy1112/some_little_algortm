def likes(names):
    if len(names) == 1:
        print(names[0] + ' likes this')
    elif len(names) == 2:
        print(names[0] + ' and ' + names[1] + ' likes this')
    elif len(names) == 3:
        print(names[0] + ' ' + names[1] + ' and ' + names[2] + ' likes this')
    else:
        print('no one likes this')

likes(['Peter'])