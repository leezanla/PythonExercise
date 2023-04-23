class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other) -> str:
        return self.name + other.name

    def __len__(self):
        return len(self.name)


stu = Student("张三")
print(stu.__len__())






























