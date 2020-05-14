list = [2,4,8,9]
def sumList(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sumList(list[1:])
print(sumList(list))