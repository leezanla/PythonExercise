# coding:utf-8
import keyword
print(keyword.kwlist)  # 打印python中的所有关键字
name = '小明'
print(id(name))
print(type(name))
print(name)
age = 19
print(name + "今年" + str(age) + "岁了")
a = True
print(int(a))

# present = input("请问你想要什么东西？\n")
# print(present, type(present))
print(1 / 2)
print(1 // 2)
x, y, z = 10, 20, 30  # 这个叫做解包赋值
x, y, z = 30, 20, 10
print(x, y, z)

# score = float(input("请输入分数：\n"))
# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("D")

for i in "hell":
    if i == 'e':
        continue
    else:
        print(i, end='')
print('\n')
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
while sum >= 5040:
    print(sum)
    sum -= 1
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(i) + '*' + str(j) + '=' + str(i * j), end='\t')
    print('\n')
