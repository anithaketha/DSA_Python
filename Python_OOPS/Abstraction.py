from abc import ABC,abstractmethod
class Car:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @abstractmethod
    def print_Detais(self):
        pass
class Audi(Car):
    def print_Details(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
car1=Audi("Anitha",19)
car1.print_Details()
