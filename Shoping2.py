shopList = {'apple' : 'pokupka1',
            'banan' : 'pokupka2',
            'meat'  : 'pokupka3',
            'water' : 'pokupka4',
            'milk'  :'pokupka5'
           }
for numb , produckt in shopList.items():
    print (produckt,':',numb )
for i in range(len(shopList)):
    produckt = input('що з цього списку ти хошеш купити')
    del shopList[produckt]
    for numb, produckt in shopList.items():
        print(produckt, ':', numb)