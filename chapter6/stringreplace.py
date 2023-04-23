s = "hello, python"
print(s.replace("python", "java"))  # hello, java
s = "hello, python, python, python"
# 指定替换的个数
print(s.replace("python", "java", 2))  # hello, java, java, python

lst = ["python", "java", "c++"]
print("、".join(lst))  # python、java、c++
print("".join(lst))  # pythonjavac++

t = ("python", "java", "c++")
print("、".join(t))  # python、java、c++
print("".join(t))  # pythonjavac++
print("*".join("python"))  # p*y*t*h*o*n



























