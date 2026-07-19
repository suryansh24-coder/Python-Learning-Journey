# Dictonaries & sets in python :-
# data in dictonaries are stored in pair of key : value 
# Dictonaries are mutable , no indexing , no ordered arrangments:-
dict = {
    "Key"  : "Value" ,
    "Name" : "Suryansh" ,
    "CGPA" : 8.52 ,
    "Marks": [92,86,85,90] ,
    "Subjects" : ["Python", "C" , "C++" , "SQL"] ,
}
info = {
    "Height" : 6 ,
    "Weight" : 80 ,
    "Hoppies" : "Coding" ,
    "Age"  : 18 ,
    "Marks" : 99.4 ,
 }
print(dict)
print(info)
print(type(dict))
print(type(info))
print(dict["Name"])
print(info["Hoppies"])
print(dict["Subjects"])
info["Name"] = "XYZ" 
print(info["Name"])
info["surname"] = "Tiwari" 
print(info)
# Empty Dictonaries :-
null_dict = {}
print(null_dict)
null_dict["Name"] = "Suryansh"
null_dict["Surname"] = "Tiwari"
print(null_dict)

# Nested Dictonaries :-
student ={
    "Name" : "Suryansh Tiwari",
    "subject" : {
        "Physics" : 82 ,
        "Chemsitry" : 99 ,
        "Maths" : 87 ,
        "English" : 100 ,
    }
}
print(student)
print(student["subject"])
print(student["subject"]["Physics"])
print(student.keys())
print(student.values())
## type casting into lists :-
print(list(student.keys()))
print(len(student))
print(list(student.values()))
## Dictonarie Methodes :-
print(list(student.keys())) # Return the keys of dictonaries
print(len(student))# return length of dictonaries
print(list(student.values())) # Return the value of dictonaries 
print(student.items()) # return the key : value pairs of dictonaries
print(student.get("Name")) # return specific value of any specific key 
student.update({"City" : "New Delhi"}) # add new key :value pair ot exisiting dictonaries
print(student)
