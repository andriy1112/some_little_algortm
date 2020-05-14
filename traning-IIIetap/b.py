with open('array-sum.in') as inps:
    lines = inps.readlines()  # Все строки
    nums = map(int, lines[1].split())   # lines[1] — вторая строка

result = sum(nums)

with open('array-sum.out', 'w') as outs:
    outs.write(str(result))           # Результат нужно преобразовать в строку


