# -*-coding:utf-8-*-
items = ['Fruits', 'Books', 'others']
prices = [98, 78, 24]
d = {item.upper(): price for item, price in zip(items, prices)}
print(d)






