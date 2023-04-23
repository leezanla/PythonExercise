lst = [1, 2, 3, 4, 5]
del lst[0]
print(lst)

dict1 = {"name": "edward", "age": 20, "gender": "male"}
del dict1["name"]
print(dict1)
for index, value in enumerate(dict1):
    print(index)
for index, value in enumerate(dict1.items()):
    print(value)









