#While loop :-
count = 1  # Iterators :
while count <=500 :
     print("Hello World", count)
     count += 1
     
print("Loop ended ! ")

x = 5 
while x >= 1 :
    print(x)
    x-=1
    
print("Loop ended !")

# WAP to print numbers from 1-100 :
i = 1 
while i<=100 :
    print(i)
    i+=1  
print("Loop ended !")

# WAP to print numbers from 100 to 1 :
i = 100 
while i>=1 :
    print(i)
    i-=1
print("Loop ended !")
    
# WAP to print the table of a number n :
i=1
n = int(input("Enter the no :"))
while i <=10 :
    print(i*n)
    i+=1 
print("Table of " ,n)

# WAP to print the series : [1,4,9,16,25,36,49,64,81,100]
i = 1 
while i<= 10:
    print(i*i)
    i+=1
print("Series printed !")
# Using methode 2 :-
nums = [1,4,9,16,25,36,49,64,81,100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx+=1

# WAP to search element in the list :  [1,4,9,16,25,36,49,64,81,100]
x = int(input("Enter the number to be searched : "))
nums = [1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(nums) :
    if(nums[i]==x) :
        print("Element found at index ",i)
    else :
        print("finding..........")
    i+=1 

# Break & Continue statement :-    
vowel = ["a","e","i","o","u"]
x = input("Enter the vowel to be serached :")
i=0
while i < len(vowel):
    if(vowel[i] == x) :
        print("Founded the element at ",i)
        break
    else :
        print("Not founded !")
    i+=1 
# Continue statement use case :-
i = 1 
while i<=10 :
    if(i%2!=0) :
        print(i)
        i+=1 
    
i = 1
while i <= 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Using For loop : for sequential traversal :-
nums = [1,2,3,4,5,6,7,8,9]
for val in nums :
    print(val)
tup =(1,2,3,4,56,855,2155,0)
for i in tup :
    print(i)
str= "SURYANSH"
for char in str :
    print(char)
# using optional else to print or do something after the completation of work:
else :
    print("Your string was : ",str)