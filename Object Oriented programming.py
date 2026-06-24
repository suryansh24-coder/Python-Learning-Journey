class Employee :
    def __init__(self):
        self.name = "Suryansh Tiwari"
        self.role = "AI Enigneer"
        self.salary = 600000
        self.language = "Python"

emp1 = Employee()
print(emp1.name)
print(emp1.role)
print(emp1.salary)
print(emp1.language)

class Student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

# Example usage:
student1 = Student("Alice", 20, "S001")
print(student1.name)
print(student1.age)
print(student1.roll_no)