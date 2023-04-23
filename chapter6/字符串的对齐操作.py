s = "hello,Python"
"""居中对齐"""
print(s.center(20, "*"))

"""左对齐"""
print(s.ljust(20, "*"))
print(s.ljust(10))  # 这个如果少的话，也会显示所有的字符
print(s.ljust(20))  # 如果不写的填充符的话，默认是空格

"""右对齐"""
print(s.rjust(20, "*"))
print(s.rjust(10))
print(s.rjust(20))

"""右对齐，使用0进行填充"""
print(s.zfill(20))






























