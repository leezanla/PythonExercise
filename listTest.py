print("下面请输入一个列表")
lis = list([])
for i in range(5):
    number = input("请输入第" + str(i + 1) + "个数：")
    lis.insert(i, number)

for j in lis:
    print(j, end="\t")









