import numpy as np 
def myadd(x,y):
    return x+y 
myadd = np.frompyfunc(myadd , 2 , 1) 
print(myadd([1,2,3,4,5],[6,7,8,9,10]))

print(type(np.add))
print(type(np.concatenate))

if (type(np.add) == np.ufunc):
    print("Yes , it is a Ufunction !!")
else :
    print("No not a Ufunction !!")






