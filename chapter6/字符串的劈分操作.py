s = "hello world python"
lst = s.split()  # 不写分隔符默认是空格
print(lst)

s1 = "hello|world|python"
print(s1.split(sep='|'))  # 指定劈分的符号
print(s1.split(sep='|', maxsplit=1))  # ['hello', 'world|python']

"""rsplit()是从右侧开始劈分"""





























