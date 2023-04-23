class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # age在类外面就不能被使用到了，加了两个下划线
        # 但是可以在类内部使用，例：

    def show(self):
        print(f"{self.name}, {self.__age}")


stu = Student("张三", 20)
stu.show()
# 在类的外部使用name与age
print(stu.name)
# print(stu.__age)  # 这个报错，AttributeError: 'Student' object has no attribute '__age'
# 可以这样使用
# print(dir(stu))  # 查看里面所有可以使用的方法
print(stu._Student__age)  # 虽然这个方法可以访问，但上面都已经加上了__，就不建议再访问了





























