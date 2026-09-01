print("FUNCTION CALCULATOR")

while True:
    print("\n1. Add 5")
    print("2. Subtract 5")
    print("3. Exit")

    choice = int(input("Choose an operation: "))

    if choice == 3:
        print("Thank you!")
        break

    if choice != 1 and choice != 2:
        print("Invalid choice!")
        continue

    x = int(input("Enter the value of x: "))

    if choice == 1:
        answer = x + 5
    elif choice == 2:
        answer = x - 5

    print("the answer is", answer)

    print("=====================")