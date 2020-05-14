d1 = 10
d2 = 20
d3 = 30

graph = {}
graph["home"] = {}
graph["home"]['shop_f'] = d1
graph["home"]["shop_s"] = d2

graph["shop_f"] = {}
graph["shop_f"]["shop_s"] = d3
graph["shop_s"] = {}

cost = {}
cost['shop_f'] = d1
cost['shop_s'] = d2

parents = {}
parents ['shop_f'] = 'home'
parents ['shop_s'] = 'home'
