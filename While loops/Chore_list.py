total_chores = 4
original_count = total_chores
print(f"you have{original_count} chores to finish today!\n")

completed_count = 0
chore_num = 1

while chore_num <= total_chores:

    if chore_num ==1: next_chore = "Make your bed"
    elif chore_num == 2: next_chore = "feed the pet"
    elif chore_num == 3: next_chore = "take out the trash"
    else: next_chore = "wash the dishes"

    answer = input(f"have you finished: {next_chore}? (yes/no):")

    if answer =="yes":
        completed_count += 1
        chore_num += 1
        print("great job! chore completed.")
    else:
        print("okay, finish it and check again!")

    print("Chores remaining:", total_chores - completed_count)
    print()

print("=====ALL CHORES COMPLETED!=====")
print("great job! you have finished your entire checklist today!!\n")

print("\n===== CHORE CHECTLIST SUMMARY ====")
print("Chores Assinged today:", original_count)
print("chores completed:", completed_count)
print("Chores remaining:", total_chores - completed_count)
print("======================================")