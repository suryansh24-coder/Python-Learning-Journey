a = 89  

def fun(): 
    global a  
    print("Value of a is:", a)  
    a = 20  
    print("Value of a inside function:", a)
    
fun()
print(a)        