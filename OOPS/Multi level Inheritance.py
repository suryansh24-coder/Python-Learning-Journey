class Car :
    # Multi - Level Inheritance :
    @staticmethod
    def start():
        print("car started.....")
        
    @staticmethod
    def stop():
        print("Car Stopped......")
    
class toyotacar(Car):
    def __init__(self,Brand):
        self.Brand = Brand
        
class fortuner(toyotacar):
    def __init__(self,type):
        self.type = type

car1 = fortuner("Diesel")
car1.start()