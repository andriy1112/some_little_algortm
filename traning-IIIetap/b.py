with open('array-sum.in') as inps:
    lines = inps.readlines()  # ��� ������
    nums = map(int, lines[1].split())   # lines[1] � ������ ������

result = sum(nums)

with open('array-sum.out', 'w') as outs:
    outs.write(str(result))           # ��������� ����� ������������� � ������


