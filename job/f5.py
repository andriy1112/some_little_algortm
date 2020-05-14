def fib_next(n):
    fib1 = 1
    fib2 = 1
    fibo_list = [fib1, fib2]
    z = n
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
        fibo_list.append(fib2)

    if z in fibo_list:
        return fib2
    else:
        raise ValueError()


print(fib_next(4))
