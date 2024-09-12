class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
    def start(self):
        self.acc=True
        self.brk=True
        print("The car has started")
car=Car()
car.start()