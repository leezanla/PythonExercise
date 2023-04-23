class Person:
    def __new__(cls, *args, **kwargs):
        print(f"__new__被调用了，cls的id值为{id(cls)}")
        obj = super().__new__(cls)
        print(f"创建的对象id为{id(obj)}")
        return obj

    def __init__(self, name, age):
        print(f"__init__方法被调用了,self的id值为：{id(self)}")
        self.name = name
        self.age = age


print(f"object这个类对象的id为{id(object)}")
print(f"Person这个类的id为{id(Person)}")

# 创建Person类的实例对象
p = Person("张三", 20)
print(f"p这个Person类的实例对象的id：{id(p)}")





























