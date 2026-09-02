print("Welcome to Function calculator!")
def add(a,b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a, b):
    return a/b

try:
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
except ValueError:
    print("Enter a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("1. Addition")
print("2. Substraction")
print("3. multiplication")
print("4. Division")

choice = input("Enter your choice:(1, 2, 3 or 4)")

if choice == "1":
    answer = add(num1, num2)
    print("The answer is:", answer)

elif choice == "2":
    answer = subtract(num1, num2)
    print("The answer is:", answer)

elif choice == "3":
    answer = multiply(num1, num2)
    print("The answer is:", answer)

elif choice == "4":
    answer = divide(num1, num2)
    print("The answer is:", answer)
    


else:
    print("Invalid input!")
    