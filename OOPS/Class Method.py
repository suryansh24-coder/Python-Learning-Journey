# Without using class Method :
class Person:
    name = "anonymous"
    
    def changeName(self,name):
        self.name = name
        
p1 = Person()
p1.changeName("Suryansh Tiwari")
print(p1.name)
print(Person.name)

class Person:
    name = "anonymous"
    
    def changeName(self,name):
        self.__class__.name = "Suryansh" # Class 
        
p1 = Person()
p1.changeName("Suryansh Tiwari")
print(p1.name)
print(Person.name)

# Using class methode :-
class person:
    name = "anonymous"
    @classmethod
    def changeName(cls , name):
        cls.name = name
        
p1 = person()
p1.changeName("Suryansh Tiwari")
print(p1.name)
print(person.name)
