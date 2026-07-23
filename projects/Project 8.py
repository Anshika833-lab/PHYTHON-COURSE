num1 = input("enter the first number:")
num2 = input("enter the second number:")
num3 = input("enter the third number:")

if num1 > num2:
    temp = num1
    num1 = num2
    num2 = temp

if num2> num3:
    temp = num2
    num2= num3
    num3 = temp

if num1 > num2:
    temp = num1
    num1= num2
    num2 = temp

    print("the correct order is: ")
    print(num1, num2, num3)
