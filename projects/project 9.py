print("**************************")
print("WELCOME TO HOLIDAY PLANNER")
print("**************************")
print()

print("Step 1: pick your holiday type")
print("1 - Beach holiday")
print("2 - Adventure holiday")
print()

choice=int(input("Choose and enter either 1 or 2: "))

if choice ==1:
    print("step 2: pick your beach activity!")
    print("1 - Swimming 🏊‍♂️")
    print("2 - Building sandcastles 🏖️")
    print()
    #Just figured out you can actually add emojis to the code!!😲

    beach_activity =int(input("enter 1 or 2:"))
    print()


    if beach_activity == 1:
        print("you picked : Swimming 🏊‍♂️")
        print("Best time  : Morning🌅")
        print("Remember   : Bring sunscreen and water🧴💦")
    else:
        print("you picked : sandcastle building 🏖️")
        print("best time  : Evening🌆")
        print("remember   : Bring shovels🪏")

 
elif choice == 2:
    print("Step 2: Pick your Adventure holiday!")
    print("  1 - Hiking")
    print("  2 - rock climbing")
    print()
 
    Adventure_activity = int(input("Enter 1 or 2: "))
    print()
 
    if Adventure_activity == 1:
        print("You picked  : Hiking")
        print("Best for    : Exploring trails")
        print("Remember    : Wear comfortable shoes")
    else:
        print("You picked  : rock climbing")
        print("Best for    : A good leg exersize")
        print("Remember    : carry a helmet")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday or 2 for Adventure Holiday.")
 
print()
print("====================================")
print("   Your holiday plan is ready!      ")
print("   Enjoy your trip and stay safe!❤️😁                ")
print("====================================")

