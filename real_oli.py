a, b, n = input().split()
a, b, n = int(a), int(b), int(n)
numb = a/b
n = str(n)
h = '%.'+n+'f'
print(h%numb)
