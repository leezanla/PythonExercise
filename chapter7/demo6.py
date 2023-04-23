def func(a, b):
    c = a + b  # c,就称为局部变量，因为c在函数体内进行定义的变量
    print(c)


# print(c)  这个会报错，因为c超出了作用的范围
# print(a)
def func1():
    global age  # 如果加上这个，就可以在函数的外部进行使用了
    age = 20
    print(age)


func1()
print(age)
