# Inherit from 2 Base class to 1 derived class :-
class A:
    varA = "Welcome to class A"
    
class B:
    varB = "Welcome to class B"
    
class C(A,B):
    varC = "Welcome to class C"
    
c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)