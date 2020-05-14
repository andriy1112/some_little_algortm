def find_palindromes(numbers):
    new_list = []
    for i in numbers:
        i = str(i)
        l = len(i)
        for k in range(l // 2):
            if i[k] == i[-1 - k]:
                if i[0] == i[len(i) - 1]:
                    new_list.append(i)

    pre_rez = set(map(int, new_list))
    return sorted(pre_rez)

print(find_palindromes([124, 121, 444, 21, 33, 44322, 956659, 9992, 33, 56743, 75357]))
