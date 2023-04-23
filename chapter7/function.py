def clac(a, b):
    return a + b


print(clac(10, 20))

# 这个与上面不一样，因为指定了关键字，就不会按顺序传参了
print(clac(b=20, a=10))

