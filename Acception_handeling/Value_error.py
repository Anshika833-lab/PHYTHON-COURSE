try:
    number= int(input("enter a number: "))
    print("the number you entered is", number)

except ValueError as ex:
    print("Exception occured:", ex)