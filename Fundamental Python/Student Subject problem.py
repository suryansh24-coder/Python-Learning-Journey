# WAP to enter marks of 3 subjects from user and store them is dictonaries. Start with an empty dictonaries & add one by one. Use subject name as key & amrks as value :-
subjects = {}
sub1 = input("Enter the name of subject 1 :")
sub2 = input("Enter the name of subject 2 :")
sub3 = input("Enter the name of subject 2 :")
marks1 = float(input("Enter the marks of subject 1 :"))
marks2 = float(input("Enter the marks of subject 2 :"))
marks3 = float(input("Enter the marks of subject 3 :"))
subjects[sub1] = marks1
subjects[sub2] = marks2
subjects[sub3] = marks3
print(subjects)
print("Total number of subjects :", len(subjects))