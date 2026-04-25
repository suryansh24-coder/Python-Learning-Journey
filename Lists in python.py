# list of marks 
marks1 = 95.6
marks2 = 85.5
marks3 = 78.5
marks4 = 99.0
marks5 = 69.7
marks = [95.6 , 85.5 , 78.5 , 99.0 , 69.7]
print(marks)
print(type(marks))
print(marks[1])

student = ["Suryansh" ,"tiwari", 69 , 18]
print(student)
student[0] = "surya"
print(len(student))

# Slicing in lists :-
marks = [1,2,3,4,5,7,6,8,9,10]
print(marks[0:4])
print(marks[2:8])
print(marks[:len(marks)])
marks.append(69)
print(marks)
marks.sort()
print(marks)
marks.sort(reverse = True)
print(marks)
marks.reverse()
print(marks)
marks.insert(8,1000) # index & value 
print(marks)

# List is our mutable data type :-
marks=['a','b','c','d','e','f','g','h','g']
print(marks[0:4])
print(marks[2:8])
print(marks[:len(marks)])
marks.append("d")
print(marks)
marks.sort()
print(marks)
marks.sort(reverse = True)
print(marks)
marks.reverse()
print(marks)
marks.insert(8,"Z") # index & value 
print(marks)

# Tuples : [] --> ( ) brackets are changed.
tup=(1,2,3,4,5,6,1,2,8,9)
print(tup)
print(type(tup))
print(tup[1])
# tup[0] = 5 : invalid for tuples .
tup=() # empty typle :
tup1=("Hello")
print(tup1)
print(type(tup1))

# Slicing in Typle : same as that of list :-
tup =(2,1,3,1)
print(tup[0:len(tup)])
# Tuple Methods :-
tup = (2,2,3,1,4)
print(tup.index(4)) # syntax :tup.index(index no)
print(tup.count(2)) # syntax :tup.count(no.to be count)
print(tup.count(4))