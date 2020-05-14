import re
something = input('print text: ')
something = something.lower()
first = len(something)
for i in range(first):
    something = something.replace(',', '')
    something = something.replace('.', '')
    something = something.replace('!', '')
    something = something.replace('?', '')
    something = something.replace(' ', '')
    something = something.replace('-', '')
    something = something.replace(':', '')
    something = something.replace(';', '')

def reverse(txt):
    return txt[::-1]


def is_palindrom(txt):
    return txt == reverse(txt)


if (is_palindrom(something)):
    print('is palindrom')
else:
    print('is not palindrom')
