try:
    a = int(input("请输入第一个数"))
    b = int(input("请输入第二个数"))
    result = a / b
except BaseException as e:
    print("输入的内容有错")
else:
    print("result = ", result)
finally:
    print("感谢来")
