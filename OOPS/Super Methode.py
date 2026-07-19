class Car:
    def __init__(self,type):
        self.type = type
        
    @staticmethod
    def start():
        print("Car started.....")
        
    @staticmethod
    def stop():
        print("Car stopped.....")
        
class ToyotaCar(Car):
    def __init__(self,brand,type):
        self.brand = brand
        super().__init__(type)
        super().start()
        
car1 = ToyotaCar("Prius","Electric")
print(car1.type)        