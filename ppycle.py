import pickle
shoplistfile = 'shoplist.data'

shoplist = ['mango', 'apple', 'banana']

f = open(shoplistfile, 'wb')

f.close()

del shoplist

f = open(shoplistfile, 'rb')


