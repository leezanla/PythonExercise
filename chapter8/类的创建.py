class Student:  # Student为类名，每个单词的首字母大写，其余小写
    native_pace = "吉林"  # 直接写在类里面的变量，称为类属性

    def __init__(self, name, age):
        # self.name称为实体属性，进行了一个赋值的操作，将局部变量的name的值赋给实体属性
        self.name = name
        self.age = age

    # 实例方法
    def eat(self):
        print("学生在吃饭...")

    @staticmethod
    def method():  # 括号里面不能写self
        print("我是静态方法")

    @classmethod
    def cm(cls):
        print("我是类方法")

# 创建Student类的对象
student = Student("小明", 18)
print(id(student))
print(type(student))
print(student)

student.eat()
# 也可以使用下面的方法来进行调用
Student.eat(student)



