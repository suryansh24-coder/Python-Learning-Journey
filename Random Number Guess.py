import random 

n = random.randint(1,100)
a =- 1
guesses = 0
while(a != n):
    a = int(input("Guess a number between 1 and 100:\t"))
    guesses += 1
    if(a < n):
        print("Almost there ! Enter the Higher number")
    else:
        print("Almost there ! Enter the Lower number")

print(f"Congratulations! You guessed the number in {guesses} guesses.")