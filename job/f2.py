def find_simple(numbers):
    new_list = []
    for i in numbers:
        j = 0
        for k in range(1, i+1):
            if i % k == 0:
                j += 1
        if j == 2:
            new_list.append(i)
    return new_list


print(find_simple(range(10)))