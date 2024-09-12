class Animal:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def Eat():
        print("I usually eat Food")
    @staticmethod
    def MakeSound():
        print("I usually make sound")
class Dog(Animal):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        # super().Eat()
        # super().MakeSound()
    def printName(self):
        return self.name
class GoldenRetriever(Dog):
    def __init__(self,breedType,name):
        self.breedType=breedType
        super().__init__(name,type)
        
    
dog1=Dog("Siberian Husky","Popularbreed")
DogType=GoldenRetriever("oneDogType","MinePersonalFav")
print(dog1.printName())
# print(dog1.name)
# print(dog1.type)
print(DogType.breedType)
print(DogType.name)