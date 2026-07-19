class Student:
    
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating objects
s1 = Student("Rahul", 20)
s2 = Student("Anita", 21)

# Calling methods
s1.display()
print()
s2.display()