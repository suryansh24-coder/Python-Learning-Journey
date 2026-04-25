# Reading , Writing and data manupliation using file I/O :-
f = open("demo.txt","r")
data = f.read()
data1 = f.read(8)
data2 = f.readline()
print(data)
print(data1)
print(data2)
print(type(data))
line1 = f.readline()
line2 = f.readline()
lines = f.readlines()
print(line1)
print(line2)
print(lines)
f.close() 

# Writing in a file :-
f = open("demo.txt","w")
data = f.write("This is new line added by write mode.")
print(data)
f.close()
# Append mode :-
f = open("demo.txt","a")
data = f.write("This is the new data added.")
print(data)
f.close()
# Over writting by "r+" mode :-
f = open("demo.txt","r+")
f.write("This")
f.close()

# With Syntax :-
with open("demo.txt","r") as f :
    data = f.read()
    print(data)
   # f.close() :- Not compulsary to write this syntax

with open("demo.txt","w") as f:
    f.write("new data")
# Deleting a file :-
# Modules are the code libraray.
import os
os.remove("sample.txt")