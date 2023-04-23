import pprint
message = "It was a bright cold day in April, and the clocks were striking thirteen"
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
dict1 = {"name": "小明", "age": 19, "gender": "man"}
print(dict1.get("name1", "小红"))
for name in dict1.keys():
    print(name)








