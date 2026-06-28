import numpy as np 
x = int(input("Enter the first number:\t"))
y = int(input("Enter the second number:\t"))
num1 = x 
num2 = y
numNew = np.lcm(num1,num2)
print(numNew)

c = np.array([3,6,9])
c1 = np.lcm.reduce(c)
print(c1)

f = np.arange(1,11)
f1 = np.lcm.reduce(f)
print(f1)




