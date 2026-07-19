# del keyword :-
class student:
    def __init__(self,name):
        self.name = name
        
s1 = student("Suryansh Tiwari")
print(s1.name)
del s1.name
print(s1.name) 

# Private (like) attributes & methods :-
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
       # self.acc_pass = acc_pass
        self.__acc_pass = acc_pass # we have maded it private using __
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = account("123456","abcde")

print(acc1.acc_no)
#print(acc1.__acc_pass)
print(acc1.reset_pass())

# Private Attributes & Private methods :-
class person:
    __name = "anonymous" # Private Attributes
    
    def __hello(): # Private Methode
        print("Hello User !")
    
    def welcome(self):
       # __hello(self.__name)
        self.__hello()
        
p1 = person()
print(p1.__name) # Error becuase it's private
print(p1.__hello)
print(p1.welcome())