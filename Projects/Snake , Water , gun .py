import random 

# Snake , Water , gun game
computer = random.choice([-1,1,0])
YourChoice = input("Enter your choice (Snake, Water, Gun):\t")
YouDict = {
    "S": 1,
    "W": 0,
    "G": -1 
}
ReverseDict = {
    1: "Snake",
    0: "Water",
    -1: "Gun"
}
you = YouDict[YourChoice]

print(f"You choosed {ReverseDict[you]} and computer choosed {ReverseDict[computer]}")

if(you == computer):
    print("Game is Draw !")
else:
    if(you == 1 and computer == 0):
        print("You Win !")
    elif(you == 0 and computer == -1):
        print("You Win !")
    elif(you == -1 and computer == 1):
        print("You Win !")
    else:
        print("Computer Wins !")
        