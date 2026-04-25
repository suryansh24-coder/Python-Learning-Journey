# Concept of recursion in python : When a function calls itself is called recursion :-
def show(n):
    print(n)
show(5)

# Recursive fuction :
def show(n):
    if n==0 :
        return # Base case !
    print(n)
    show(n-1) # Recursion ! 
show(5)
show(50)

# WAP for factorial using recursion :-
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n* fact(n-1)

n= int(input("Enter the number whose factorial you want : \t"))
print(fact(n))

# WAP using recursive fucntion to calculate the sum of first n natural numbers:-
def sum_naturalNum(n):
    if(n==0):
        return 0
    return sum_naturalNum(n-1) + n
    
sum = sum_naturalNum(5)
print(sum) 
    
# WAP using recursive fucntion to print all the elements in list :-
def print_list(list,idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
list = ["Mango" ,"Apple", "Guavava","Lichi","Banana","Pear","Papaya"]

print_list(list)
