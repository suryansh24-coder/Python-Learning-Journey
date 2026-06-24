for i in range(11): 
    print(i)  
 
names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Reyansh", "Krishna", "Ishaan", "Shaurya", "Atharv",
    "Ayaan", "Kabir", "Rudra", "Aryan", "Dhruv", "Ansh", "Kartik", "Yuvraj", "Dev", "Harsh",
    "Rohan", "Kunal", "Siddharth", "Rahul", "Aman", "Nikhil", "Varun", "Manav", "Parth", "Tanish",
    "Rishi", "Laksh", "Pranav", "Om", "Abhay", "Arnav", "Aakash", "Rajat", "Gaurav", "Deepak",
    "Rakesh", "Saurabh", "Vikas", "Mohit", "Sumit", "Ajay", "Vijay", "Akash", "Ravi", "Piyush",
    "Ananya", "Aadhya", "Diya", "Siya", "Myra", "Anika", "Kavya", "Navya", "Ira", "Kiara",
    "Sara", "Riya", "Pari", "Meera", "Saanvi", "Aarohi", "Avni", "Naina", "Ishita", "Tanvi",
    "Shruti", "Pooja", "Neha", "Priya", "Sneha", "Kritika", "Muskan", "Simran", "Aarti", "Payal",
    "Komal", "Rashmi", "Nidhi", "Shreya", "Palak", "Ritika", "Khushi", "Nandini", "Divya", "Bhavna",
    "Preeti", "Jyoti", "Madhuri", "Ruchi", "Swati", "Anjali", "Vaishnavi", "Sakshi", "Mansi", "Prerna"
]
n = input("Enter the letter from which you want names :\t")
for name in names:
    if name.startswith(n):
        print(f"Hello {name}!")