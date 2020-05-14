import random
money = input('how much money do you have $$$ ')
ost = 0
int(money)
shopList = {'apple' : random.randint(1,5),
            'banan' : random.randint(1,5),
            'meat'  : random.randint(1,5),
            'water' : random.randint(1,5),
            'milk'  :random.randint(1,5)
           }
for produckt , numb  in shopList.items():
    print (produckt,':',numb,'$' )
for i in range(len(shopList)):
    produc = input('що з цього списку ти хошеш купити ')
    ost += shopList[produc]
    if ost >0:
        del shopList[produc]
        for produckts, numbs in shopList.items():
            print(produckts, ':', numbs,'$')
    else:
        print('you have no money')
print('ти скупився на ' , ost , '$')
print('остача - ', int(money)-ost)