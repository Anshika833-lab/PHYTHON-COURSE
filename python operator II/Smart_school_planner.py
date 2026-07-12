print("=== smart school day planner===")
print("Answer 3 quick questions and I will plan your day!/n")

day= input("what day is it? (monday to sunday):"). strip().capitalize()
weather= input("what is the weather?(sunny / rainy / cloudy):").strip().lower()
homework= input("Is your homework done? ( yes/no): ").strip().lower()

print()
print(f"===your plan for the {day} ===")
print("-" * 35)

if day in ("saturday","Sunday"):
    print("day type  : weekend - enjoy your free time!")
elif day == "Monday":
    print("day type  : first day of the week. pack your weekly planner.")
elif day == "Friday":
    print("day type  : last day of the week. return library books today.")
elif day == "Thursday":
    print("day type ")