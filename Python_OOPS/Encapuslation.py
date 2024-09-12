class Bank:
    def __init__(self,account,Balance):
        self._account=account
        self.__Balance=Balance
    def get_Balance(self):
        return self.__Balance
    def set_Balance(self,Balance):
        if Balance>0:
            self.__Balance=Balance
        else:
            print("Invalid Balance")
Customer1=Bank(6080,20000)
print(Customer1._account)
# print(Customer1.__Balance) ##It will raise an attribute error as it is private . 
print(Customer1.get_Balance())
Customer1.set_Balance(3000)
print(Customer1.get_Balance())
