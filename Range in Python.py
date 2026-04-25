# Range function returns the sequence of number from 0 by default and increment by 1 :-
for el in range(10) :
    print(el)
seq = range(40)
for i in seq :
    print(i)
# Formating : range(start,stop ,step) :-
for i in range(2,10) :
    print(i)
for i in range(2,21,2) :
    print(i)
for i in range(10) :
    print(i)
for i in range(2,100,8) :
    print(i)
# WAP to print the element of the following list using a loop :-
lis=[1,4,9,16,25,36,49,64,81,100]
for i in range(10):
    print(list[i])
# WAP to print number from 1 to 100 :-
for i in range(1,101,1) :
    print(i)
# WAP to print numbers from 100 to 1 :-
for i in range(100,0,-1) :
    print(i)
# WAP to print the table of any number n :-
n =int(input("Enter the number : "))
for i in range(1,11,1) :
    print(i*n)

# Pass statement in python :-
for i in range(5):
    pass  ## it is use for placeholder for future code !
print("Some useful work")

# WAP to find the sum of first n numbers using while statement :
i=0 
sum =0
n = int(input("Enter the the number till which you want sum : "))
for i in range(1,n+1):
    sum += i
    print(sum)

# WAP to find the factorial of first n numbers :-
n = int(input("Enter the number :"))
fact = 1 
i=1 
while i<=n :
    fact*=i
    i+=1
    print("Factorial :",fact)