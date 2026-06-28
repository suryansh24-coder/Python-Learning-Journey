import numpy as np 

x = np.array([1,2,3,4,5,6])
for i in x :
    print(i) 
    
import numpy as np 

y = np.array([[1,2,3],[4,5,6]])
for i in x :
    print(i)    
    
import numpy as np 

s = np.array([[1,2,3],[4,5,6]])
for i in s :
    for j in i :
        print(j)    
     
     
import numpy as np 

t = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
for i in t :
    for j in i :
        for x in j :
            print(x)
            
for i in t :
    print(i)
    
for i in t :
    for j in i:
        print(j)  
           
import numpy as np 

q = np.array([[[1,2],[3,4],[5,6],[7,8],[9,10],[11,12],[13,14],[15,16]]]) 
for i in np.nditer(q):
    print(i)          
           
import numpy as np 
r = np.array([[1,2,3,4],[5,6,7,8]])
for i in np.nditer(r[:,::2]):
    print(i)    
            
              
               
                
                
                 
                 
                   
                    
                     
                      