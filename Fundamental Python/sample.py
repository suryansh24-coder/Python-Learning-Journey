# Program to calculate total, average, and grade of a student

# Input marks
name = input("Enter student name: ")
m1 = float(input("Enter marks in Subject 1: "))
m2 = float(input("Enter marks in Subject 2: "))
m3 = float(input("Enter marks in Subject 3: "))

# Calculation
total = m1 + m2 + m3
average = total / 3

# Grade logic
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "F"

# Output
print("\n--- Student Report ---")
print("Name      :", name)
print("Total     :", total)
print("Average   :", average)
print("Grade     :", grade)

