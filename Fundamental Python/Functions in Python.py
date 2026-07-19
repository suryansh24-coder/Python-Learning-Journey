# Concept of functions in python:-
def sum(a,b):
     sNum = a+b
     print(sNum)
     return sNum
 
sum(5,10)
def print_Hello():
    print("Hello World")
print_Hello()
# WA Program for avg of 3 numbers :-
def Avg_Nums(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg
Avg_Nums(5,4,6)

# Type of functions in python :
print("Suryansh",end="$")
print("Tiwari")
# Default Arguments :-
def cal_product(a=1,b=5):
    print(a*b)
    return a * b

cal_product(5,10)
cal_product()
cal_product(5,)
cal_product(10)

# WAF to print the lenght of a list & add city in list :-
city = ["New Delhi","Mumbai","Punjab","Chhatishghar","Bihar"]
def list_len(city):
    print(len(city))
    return len(city)
def add_list():
    New = input("Enter the city you want to add :\n")
    city.append(New)
    print(city)
    return city
list_len(city)
add_list()

# WAF to print the elements of a list in a single line.(list is the parameter)
course = ["CSE","AI-ML","DS","MECH","CIVIL"]
def display_elements(course):
   for item in course:
    print(item, end=" ")
    
display_elements(course)

# WAF to find the factorial of n.(n is the parameter):-
def factorial(num):
    fact=1
    for i in range(1,num+1):
       fact*=i
       print(fact)
num = int(input("Enter the number : \t"))
factorial(num)

# WAF to convert USD to INR :-
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")
    
converter(1000)
converter(56.896)

# WAF that take num as input if it is odd string output odd else even:-
def check_OddEven(num):
    if (num%2==0):
        print("Even")
    elif(num%2!=0):
        print("Odd")
    else:
        print("Enter a valid number!")
        
num = int(input("Enter a number : \t"))
check_OddEven(num)