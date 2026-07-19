try: 
    a = int (input ("Enter a Number : "))
    print(a)
    
except ValueError:
    print ("Invalid input. Please enter a valid integer.") 
    
except Exception as e:
    print(e)
    
print ("End of Program")   

print("-------------------------------------------------------------------")

a = int (input ("Enter a Number : "))
b = int (input ("Enter another Number : "))

if(b == 0):
    raise Exception("Division by zero is not allowed.")

else: 
    print(f"The result of {a} divided by {b} is: {a / b}") 

print("-------------------------------------------------------------------")

try :
    a = int(input("Enter a Number : "))
    print(a)
     
except Exception as e:
    print(e)
    
finally:
    print ("End of Program")
    print("Bye Bye !!")     