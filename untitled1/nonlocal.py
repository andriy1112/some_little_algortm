def func():
    x = 2
    print('x = ', x)

    def func2():
        nonlocal x
        x = 5

    func2()
    print(' x = ', x)
