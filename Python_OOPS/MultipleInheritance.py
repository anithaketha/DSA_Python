class Animal:
    @staticmethod
    def makeSound():
        print("I usually make sound , it's my way of communication")
        
    @staticmethod
    def eat():
        print("I eat food")
class Dog(Animal):
    def __init__(self,name):
        self.name=name
    def printName(self):
        return self.name
class SiberainHusky(Dog):
    def __init__(self,type):
        self.type=type
dog1=Dog("Golden Retriever")
dog2=Dog("German Shepered")
DogType=SiberainHusky("PopularBreed")
print(DogType.type)
DogType.eat()
print(dog1.name)
print(dog2.name)
dog1.eat()
dog2.makeSound()
