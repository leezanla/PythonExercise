def func(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)
    print("d = ", d)


# 调用func函数
# func(10, 20, 30, 40)  # 位置实参传递
func(a=10, b=20, c=30, d=40)  # 关键字传递
"""现在有一个需求，c,d只能采用关键字传递"""
func(10, 20, c=30, d=40)

"""函数定义时的形参的顺序问题"""
# def func(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递

def func1(a, b, *, c, d, **args):
    pass

def func2(*args, **args1):
    pass

def func3(a, b=10, *args, **args1):
    pass
