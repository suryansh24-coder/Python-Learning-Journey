# If-elif-else :-
name = input("Enter the name : ")
age = int(input("Enter the age : "))

if(age>=18):
    print("Eligible for voting !")
elif(age<18):
    print("You are not eligible !")
else :
    print("Enter a valid age !")

# Red light 
signal = input("Enter the signal :")
if(signal == "red"):
    print("stop")
elif(signal == "Yellow"):
    print("Wait")
elif(signal == "Green") :
    print("Go")
else :
    print("Enter a valid colour.")
    
# Nested if-else :-
age = 24
if(age>=18) :
    if(age>=80) :
      print("Cannot drive !")
    else :
        print("Can drive")
else :
    print("Cannot drive")
