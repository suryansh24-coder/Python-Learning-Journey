class Car :
    color = "black"
    @staticmethod
    def start():
        print("car started.....")
        
    @staticmethod
    def stop():
        print("Car Stopped......")
    
class toyotacar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = toyotacar("Fortuner")
car1 = toyotacar("Prius")

print(car1.start())
print(car1.stop())
print(car1.color)