def func(a, b, c):
    print("a = ", a)
    print("b = ", b)
    print("c = ", c)


lst = [10, 20, 30]
# 如何让lst中的值传入对应的形参a, b, c上，只需要加上一个 * 即可
func(*lst)

dic = {"a": 100, "b": 200, "c": 300}
func(**dic)  # 这个需要加上 ** 即可传入





























