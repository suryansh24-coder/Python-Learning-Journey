# sets in python are collection of unordered items :-
# Each items in the set must be unique & immutable :-
collections ={1,2,3,4,5,6,7,8,9,10}
print(collections)
print(type(collections))
collections2 ={1,1,2,2,10,"World"}
print(collections2)
print(type(collections2))
print(len(collections2))

# Creation of Empty sets :-
collection3 ={}
print(collection3)
collection4 = set()
print(collection4)
collection4.add(1) #collection4.add()-> add value 
collection4.add(2)
collection4.add(4)
collection4.add(58)
print(collection4)
collection4.remove(1)  # collection4.remove() --> remove value
collection4.add("Suryansh Tiwari") # we can pass everything but we can't pass any list value.
print(collection4)
collection4.pop() # removes random value.
print(collection4)
collection4.pop()
print(collection4)
collection4.clear() # empeties the set.
print(collection4)
print(len(collection4))

# Concept of Union & Intersection in sets :-
set1 = {1,2,3,4}
set2 = {4,5,6,7}
print(set1.union(set2)) # Union
print(set1.intersection(set2)) # Intersection