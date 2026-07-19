# Indexing in python : (Positive Indexing)
# [0,1,2,3,4,5,6,7,8,9,10,.....] -> Help in access characters :
str = "Suryansh Tiwari"
ch = str[0]
print(ch)

# Slicing : Accessing components of string.
str = "Suryansh Tiwari"
str[0:8]
print(str)
print(str[0:8])
print(str[5:9])
print(str[8:14])
print(str[0:len(str)])
print(str[ :len(str)])
print(str[0 : ])

# Slicing by negative index :-
# [.....,-5,-4,-3,-2,-1] <-
str = "Suryansh Tiwari"
print(str[-5 : -1])
print(str[-8 : -1])
print(str[-10 :-1])
print(str[  :-1])
print(str[-5: ])

# Functions in string:-
str = "Suryansh Tiwari"
print(str.endswith("ari"))
print(str.endswith("zyx"))
print(str.capitalize())
str = str.capitalize()
print(str.replace("Tiwari","Tripathi"))

str = "c,cpp,python,java.javascript,angular,c#,kotlin,html,css"
print(str.find("python")) # print the starting index of that.
print(str.find("c#"))

str2 = "I,O,I,O,I,O,I,O,I,I,O,O,I,I,I,O,I,O,O,I,O,O,I,O"
print(str2.count("O"))
print(str2.count("I"))

# WAP to print the len of string after taking it input form user:-
name = input("Enter the name :")
print(name)
print(len(name))

# WAP to find the occurance of s in any string:
str = input("Enter the name : ")
print(str.count("s"))