class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}正在吃饭")


stu1 = Student("张三", 18)
stu2 = Student("李四", 20)
# 为stu2动态绑定性别属性，性别属性在上面没有
stu2.gender = "女"
print(stu1.name, stu1.age)
# 若stu1也想打印性别，会报错
# print(stu1.gender)  # AttributeError: 'Student' object has no attribute 'gender'
print(stu2.name, stu2.age, stu2.gender)

# 定义在类外的方法
def show():
    print("定义在类之外的方法")

stu1.show = show
stu1.show()

def fun(student):
    print(student.name)

fun(stu1)



























