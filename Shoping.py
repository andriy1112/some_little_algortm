ShopList = ['apple', 'banan',  'candy',  'meat', 'water']
numb = 1
for item in ShopList:
    print(numb, item)
    numb += 1
numb = 1
for i in range(5):
    delname = input('що хочеш купити')
    if delname == 'apple':
        del ShopList[0]
        for itm in ShopList:
            print(numb, itm)
            numb += 1
    numb = 1
    if delname == 'banan':

        del ShopList[0]
        for m in ShopList:
            print(numb, m)
            numb += 1
    if delname == 'candy':
        numb = 1
        del ShopList[0]
        for m in ShopList:
            print(numb, m)
            numb += 1
    if delname == 'meat':
        numb = 1
        del ShopList[0]
        for m in ShopList:
            print(numb, m)
            numb += 1
    if delname == 'water':
        numb = 1
        del ShopList[0]
        for m in ShopList:
            print(numb, m)
            numb += 1
print('с покупками закінчено MR.STARK')