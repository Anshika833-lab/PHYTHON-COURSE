import random 
import math
print("======RANDOM FUN CALCULATOR======")
random_number = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"your lucky number is: {random_number}")

fun_choices = random.choice(["walking", "drawing", "painting", "reading","swimming"])
print(f"your fun activity is: {fun_choices}")

secret_number = random.randint(1, 5)
while True:
    guess = int(input("guess the secret number from 1 to 5, give me your best guess:"))
    if guess == secret_number:
        print(f"\ncongratulations, you guess the secret number! The number was {secret_number}")
        break
    else:
        print("that is not correct, try again!")
        continue

decimal_number = float(input("enter a decimal number: "))
print(f"floor value of your decimal number is: {math.floor(decimal_number)}")

x = 15
y = -10

print("copy sign results:", math.copysign(x, y))

negative_number = int(input("Enter a negative number: "))
print("Absolute value:", math.fabs(negative_number))


num1 = int(input("Enter first number for GCD: "))
num2 = int(input("Enter second number for GCD: "))

print("GCD is:", math.gcd(num1, num2))

print("\n===== FUN CALCULATOR SUMMARY =====")
print("Lucky Number:", random_number)
print("Random Activity:", fun_choices)
print("Secret Number:", secret_number)
print("==================================")


      
