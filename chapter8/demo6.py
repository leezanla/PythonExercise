class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
# 创建一个C类的对象
x = C("Jack", 18)  # c是C类型的一个实例对象
print(x.__dict__)  # 绑定的是实例对象的属性字典
print(C.__dict__)  # 类对象的属性和方法
print("-----------------")
print(x.__class__)  # 输出对象所属的类
print(C.__bases__)  # 输出的是父类类型的元素
print(C.__base__)  # 输出最近的一个类
print(C.__mro__)  # 类的层次结构
print(A.__subclasses__())  # 查看一个类的子类

