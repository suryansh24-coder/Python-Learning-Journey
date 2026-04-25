# Complex Numbers :
class Complex :
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img 
        return complex(newReal,newImg)   
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img 
        return complex(newReal,newImg)  
    
    def __multi__(self,num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img 
        return complex(newReal,newImg) 
           
num1 = Complex(1,3)
num1.showNumber()    
num2 = Complex(2,4)
num2.showNumber()
num3 = num1.add(num2)
print(num3)