str1 = "This is first string."
str2 = "This is second string."
str3 = "This is third string."
str4 = 'This is rohan"s room'
# Escaping sequence character : new line , tab etc.
st1 = "This is my first line.\nThis is my second line."
print(st1)
st1 = "This is my first line.\tThis is my second line."
print(st1)

# Concatination of strings :-
name ="Suryansh"
surname = "\tTiwari"
Full_nam = name + surname
print(Full_nam)
print(len(Full_nam))
print(len(name))

# Some comands :-
text = "hello World"

print(text.upper())    # HELLO WORLD
print(text.lower())    # hello world
print(text.title())    # Hello World
print(text.capitalize())  # Hello world

text = "I like Java"

print(text.replace("Java", "Python"))  