# WAP to print the element of following list using loop :[1,4,9,16,25,36,49,64,81,100]
given = [1,4,9,16,25,36,49,64,81,100]
for i in given :
    print(i)

# WAP to search for a number x in this tuple using loop :
tup =(1,4,9,16,25,36,49,64,81,100)
print(tup)
x= int(input("Enter the number to be searched : "))
idx = 0
for i in tup :
    if (x==i) :
        print("Element succesfully found at : ",i)
        idx+=1
        break 
    else :
        print("Element is not present !")
else :
    print("End of program !")