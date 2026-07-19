print("Hello World")
print("Lovely wheater today !")
# Basic Print statements in python
s = "Python"
s.upper()
s.lower()
s.replace("p","P")
len(s)
print(s)
# String operations :
nums = [10, 20, 30]
nums.append(40)
nums.remove(20)
print(nums)
# updatation & deletation
s = {1, 2, 3, 3}
print(s)   # duplicates removed
student={
    "Name":"Suryansh Tiwari",
    "Roll no.":85115,
    "Marks":"85",    
}
print(student["Name"])
print(student["Roll no."])
print(student["Marks"])
# File Handling I/O :
f=open("Basic.txt","a")
print(f.write("Hello World"))
f.close()
