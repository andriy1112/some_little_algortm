import pickle
a_book = 'adrress_Book.data'
want = input('''
1. Переглянути
2. Добавити
3. Редагувати
4. Видалити
5. Шукати \n''')

ab = { 'Міша'    : 'В центрі, навпроти міні-маркета',
       'Олексій' : 'на горкуті'
    }
if want == 'Добавити':
    name = input('Як звати ващого друга? \n')
    address = input('Де він проживає? \n')
    ab[name] = address
    f = open(a_book, 'wb')
    pickle.dump(ab, f)
    f.close()
    for name, address in ab.items():
        print('{0}, живе {1}'.format(name, address))
if want == 'Видалити':
    delname = input('Kого ви бажаєте видалити? \n')
    del ab[delname]
    f = open(a_book, 'wb')
    pickle.dump(ab, f)
    f.close()
    for name, address in ab.items():
        print('{0}, живе {1}'.format(name, address))
if want == 'Редагувати':
    red_name = input('Адрес якого друга ви бажаєте змінити? \n')
    red_adrress = input('його новий адрес \n')
    ab[red_name] = red_adrress
    f = open(a_book, 'wb')
    pickle.dump(ab, f)
    f.close()
    for red_name, red_address in ab.items():
        print('{0}, живе {1}'.format(red_name, red_address))
if want == 'Переглянути':
    f = open(a_book, 'rb')
    stored = pickle.load(f)
    print(stored)
if want == 'Шукати':
    search = input('Чий адрес ви хочете дізнатися? \n')
    print(search, 'живе', ab[search])
