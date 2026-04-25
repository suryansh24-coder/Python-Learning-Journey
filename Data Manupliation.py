# create a new file "practice.txt" using python. Add some data :-
# Hi everyone
# we are learning file I/O
# using java 
# I like java programming
with open ("practice.txt","w") as f:
    f.write("Hi everyone \nWe are learning file I/O\n")
    f.write("using java.\nI like programming in Java.\n")
    f.close()

# WAF that replaces all occurance of "java" with "python" in above file :-
with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("java","python")
    print(new_data)
    
with open("practice.txt","w") as f:
    f.write(new_data)

# Search if the word "learning" exists in the file or not :-
word = "learning"
with open("practice.txt","r") as f:
     data = f.read()
     if(data.find(word) != -1):
         print("Found !")
     else :
         print("Not found !")

# Makign code as a function :-

def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
     data = f.read()
    if(data.find(word) != -1):
         print("Found !")
    else :
         print("Not found !")

# WAF to find in which line of the file does the word "learning" occurs first print -1 if word not found :
def check_for_line():
    word = input("Enter the word want to search :\t")
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data :
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1

print(check_for_line())


# From a file containgn numbers separated by comma , print the count of even numbers :-
with open("sample_data.txt","r")as f :
    data = f.read()
    print(data) 
    
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(num)
            num = ""
        else:
            num += data[i]