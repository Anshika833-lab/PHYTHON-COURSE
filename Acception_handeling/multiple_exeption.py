try:
    num1, num2 = eval(input("Enter two numbers, seperated by a comma:"))
    result = num1/num2
    print("Result is", round(result, 2))

except ZeroDivisionError:
    print("Division by zero is error!!")
except SyntaxError:
    print("Comma is missing. Enter numbers seperated by comma like this: 1, 2")
else:
  print("No exceptions")
finally:
    print("this will execute no matter what!")


 