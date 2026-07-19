# Property Decorator :-
class Student:
    def __init__(self,phy,chem,maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
        
    def calPercentage(self):
        self.percentage = str((self.phy + self.chem + self.maths)/3) + "%"
       
stu1 = Student(99,100,94)
print(stu1.percentage)
stu1.phy = 86
print(stu1.phy)
print(stu1.percentage)
stu1.calPercentage()
print(stu1.percentage)

# Solving using Property decorator :-
class Student:
    def __init__(self,phy,chem,maths):
        self.phy =phy 
        self.chem = chem
        self.maths = maths
        
    @ property
    def percentage(self):
        return str((self.phy + self.chem + self.maths)/3) + "%"
    
stu1 = Student(99,98,96)
print(stu1.percentage)
stu1.phy = 86
print(stu1.percentage)