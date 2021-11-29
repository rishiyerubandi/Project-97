import random

print("Number Guessing Game")

number = random.randint(1,9)
chances = 0

print("Guess a Number between 1 and 9")
while chances < 5:
    guess = int(input("Enter your guess: "))

    if guess==number:
        print("Congratulations, You Won!")
        

    elif guess<number:
     print("Your guess was too low: ", guess)

    else:
     print("Your guess was too high: ", guess)
    chances += 1

    if not chances < 5: 
        print("YOU LOSE!!! The number is", number)