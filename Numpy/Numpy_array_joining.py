import numpy as np 
x = np.array([1,2,3,4,5,6])
x1 = np.array([7,8,9,10,11,12])
y = np.concatenate((x,x1))
y1 = np.concatenate((x1,x))
y2 = np.concatenate((x,x))

print(y)
print(y1)
print(y2)

print("\n")

import numpy as np 
g = np.array([[1,2,3],[4,5,6]])
g1 = np.array([[7,8,9],[10,11,12]])
g3 = np.concatenate((g,g1) , axis=1)
print(g3)    
print("\n")

import numpy as np 
f = np.array([1,2,3]) 
f1 = np.array([4,5,6])
f3 = np.stack((f,f1), axis= 1 )
print(f3)              
print("\n")  
    
import numpy as np
f4 = np.array([1,2,3])
f5 = np.array([4,5,6])
f6 = np.hstack((f4,f5))
f7 = np.vstack((f4,f5)) 
f8 = np.dstack((f4,f5))
print(f6)
print(f7)
print(f8)
                   
                     
                      
                         
                          
                           
                            
                             
                              
                               
                                
                                    

