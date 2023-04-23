def func(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)

    return odd, even


# 函数的调用
lst = [10, 29, 34, 23, 44, 53, 55]
print(func(lst))
"""
    上面的结论我们可以得到
        1、如果函数没有返回值， return 可以不写
        2、函数的返回值，如果是1个，直接返回类型
        3、函数的返回值，如果是多个，返回的结果为元组
"""






























