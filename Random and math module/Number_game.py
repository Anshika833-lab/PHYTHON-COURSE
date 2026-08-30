import random
number = str(random.randint(0,5))
print("the game ends when you get 1 hero!")

while True:
    guess = input("give me your best guess\n")
    if number == guess:
        print("you win the game!")
        print("The nubmer was", number)
        break
    else:
        print("your guess isn't quite right, try again!\n")

