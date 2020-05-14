phoneBook = dict()
phoneBook['Misha']   = 380686199340
phoneBook['Oleksiy'] = 380975658599
phoneBook['Nazar']   = 380977740568
name = input('чий номер телефону тебе цікавить - ')
def book(phoneBook , name):
    if name in phoneBook:
        return phoneBook[name]
    else:
        print('цього імені нема в списку')
book(phoneBook , name)
print(book(phoneBook , name))