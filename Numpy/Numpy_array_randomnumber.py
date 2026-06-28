import numpy as np 
from numpy import random
x = random.randint(100)
print(x)
x1 = random.rand()
print(x1)

n = int(input("Enter the size :"))
y = random.randint(100 , size=(n))
print(y)


z = random.randint(100 , size= (3,5))
print(z)

z1 = random.rand(3,5)
print(z1) 

c = random.choice([4,5,2,8,963,525,525,10,225,36,22545,169.159])
print(c)

c1 = random.choice([4,5,2,8,963,525,525,10,225,36,169,159] , size=(3,5))
print(c1)











