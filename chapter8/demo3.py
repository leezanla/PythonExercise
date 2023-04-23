class Person(object):  # Person继承object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"{self.name}, {self.age}")


class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):
        super().info()
        print(f"{self.stu_no}")


class Teacher(Person):
    def __init__(self, name, age, teach_of_year):
        super().__init__(name, age)
        self.teach_of_year = teach_of_year

    def info(self):
        super().info()
        print(f"{self.teach_of_year}")

stu = Student("小明", 18, 2019)
stu.info()





























