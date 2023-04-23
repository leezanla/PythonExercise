"""第一种方式，使用（）"""
t = ("python", "world", 98)
# 上面的小括号可以省略不写
t2 = "python", "world", 98

print(t)
print(type(t))


"""第二种创建方式，使用内置函数tuple()"""
t1 = tuple(("python", "world", 98))
print(t1)
print(type(t1))


# 如果元组中只有一个元素，小括号和逗号都不能省略不写
t3 = ("python", )
print(t3)
print(type(t3))


























