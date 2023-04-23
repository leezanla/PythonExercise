"""第一种方式 使用 % 的形式"""
name = "张三"
age = 20
print("我叫%s, 今年%d岁" % (name, age))


"""第二种方式 使用 {} 的形式"""
print("我叫{0}, 今年{1}岁".format(name, age))


"""第三种方式 f-string形式"""
print(f"我叫{name}, 今年{age}岁")



