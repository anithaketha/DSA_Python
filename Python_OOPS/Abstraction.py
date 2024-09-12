from abc import ABC,abstractmethod
class College:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def print_Detais(self):
        pass
class Student(College):
    def print_Details(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
stu1=Student("Anitha",19)
stu1.print_Details()
