m ={'''Empty Dictionary'''}
marks ={
    "Suryansh" : 100 ,
    "Rohit" : 90 ,
    "Sam" : 80 ,
    "Arjun" : 70 ,
    "Shivam" : 60 ,
    "Parul" : 50 ,
}
print(marks, type(marks))
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohit": 91, "Aanchal": 99})
print(marks)
print(marks.get("Rohit"))

Set = {1, 2, 3, 4, 5}