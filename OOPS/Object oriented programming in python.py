## Creating class and objects :-
class student : # class
    name = "Suryansh Tiwari"
    
s1 = student() #Creating Objects (instance)
print(s1)
print(s1.name)
s2 = student()
print(s2.name)

class car:
    color = "blue"
    brand = "Mercedes"
    
car1 = car()
print(car1.color)
print(car1.brand)

# Concept of constructor in python oops :-
class student: 
    def __init__(self , fullname):
        self.name = fullname
        print("Adding new student in Database......")
        
s1 = student("Suryansh Tiwari")
print(s1.name) # Suryansh Tiwari

class student: 
    # default constructor :-
    def __init__(self):
        pass
    # Parameterized constructor :-
    def __init__(abcd , fullname ,marks): # self can be changed to abcd , becuase it's  a alias ! 
        abcd.name = fullname
        abcd.marks = marks
        print("Adding new student in Database......")
        
s1 = student("Suryansh Tiwari",99)
print(s1.name,s1.marks) # Suryansh Tiwari
s2 = student("Karan Aujla",100)
print(s2.name,s2.marks) # Data stored is called attributes :- 

# Class & instance Attributes :-
class student: 
    college_name = "JSS University"# class Atrubute
    # default constructor :-
    def __init__(self):
        pass
    # Parameterized constructor :-
    def __init__(abcd , fullname ,marks): # self can be changed to abcd , becuase it's  a alias ! 
        abcd.name = fullname
        abcd.marks = marks
        print("Adding new student in Database......")
        
s1 = student("Suryansh Tiwari",99)
print(s1.name,s1.marks)
print(s1.college_name)

s2 = student("Karan ",100)
print(s2.name,s2.marks)
print(s2.college_name)
print(student.college_name) # we caN USE  this as well class.atributes
# obj attr > class attr

# Methods in python under OOPS:
class student :
    def __init__(self,fullname):
        self.name = fullname
    def hello(self):
        print("Hello",self.name)
    def welcome(self):
        print("Welcome",self.name)
    def marks(self):
        return self.marks
    
s1 = student("Suryansh")
s1.hello()
s1.welcome()
print(s1.marks)
 
 
# Create a student class that takes name and marks of 3 subjects as arguments in constructor then create a methode to print the average of it :
class result:
    def __init__(self , Name , marks):
        self.name = Name
        self.marks = marks
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"your average score is :\t",sum/3)
s1 = result("Suryansh",[99,87,80])
s1.get_avg()

# Static Methodes :-
class result:
    def __init__(self , Name , marks):
        self.name = Name
        self.marks = marks
        
    @staticmethod # Decorator
    def hello():
        print("Hello World !")
    def get_avg(self):
        sum = 0 
        for val in self.marks:
            sum+=val
        print("Hi",self.name,"your average score is :\t",sum/3)
s1 = result("Suryansh",[99,87,80])
s1.get_avg()
s1.hello()

# Miscellanious topics of OOPS in python: -
class car: # Abstraction Example
    def __init__(self):
        self.acc = False 
        self.brk = False
        self.clutch = False
    def start(self): # Hidden Implementation details
        self.clutch = True
        self.acc = True
        print("Car Strated.....") 
        
car1 = car()
car1.start()

## WAP to create account class with 2 attributes - balance & account no. create methodes for debit , credit & printing the balance :- 
class account:
    def __init__(self,balance,accNum):
        self.balance = balance
        self.an = accNum
        
    # Debit Methode
    def debit(self, ammount):
        self.balance -= ammount
        print("Rs.",ammount,"was debited")
        print("Total Balance : \t",self.get_Balance)
        
    # Credit Methode
    
    def credit(self, ammount):
        self.balance += ammount
        print("Rs.",ammount,"was credited")    
        
    # Show Balance
    def get_Balance(self):
        return self.balance
    
acc1 = account(1000,12345)
print(acc1.balance)
print(acc1.an)
acc1.debit(1000)
acc1.credit(100)
