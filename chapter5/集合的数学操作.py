s1 = {10, 20, 30, 40}
s2 = {20, 30, 40, 50, 60}

# 交集 (交集之后的集合也没有发生改变)
print(s1.intersection(s2))  # {40, 20, 30}
# 也可以使用下的 & 符号
print(s1 & s2)

# 并集操作 (并集之后的集全也没有发生改变)
print(s1.union(s2))  # {40, 10, 50, 20, 60, 30}
# 也可以使用下的 | 符号
print(s1 | s2)

# 差集操作
print(s1.difference(s2))  # {10}
print(s1 - s2)

# 对称差集
print(s1.symmetric_difference(s2))  # {40, 10, 50, 20, 60, 30}
print(s1 ^ s2)



























