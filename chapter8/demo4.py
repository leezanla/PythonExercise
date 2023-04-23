class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"我的名字是{self.name},今年{self.age}"


stu = Student("张三", 19)
print(stu)  # 我的名字是张三,今年19   不会再写内存地址了
