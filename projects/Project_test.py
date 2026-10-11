print("====== Welcome to student grade book ======")
student = {}
student["Alice"] = [85, 90, 78]
student["Charlie"] = [92, 88, 95]
student["Bob"] = [78, 82, 85]
student["David"] = [90, 85, 92]
student["Elena"] = [34, 65, 98]

print("====== Student Grades ======")
for name, grades in student.items():
    average = sum(grades) / len(grades)
    print(f"Name: {name}, Grades: {grades}, Average = {average:.2f}")

    Top_scorer = max(student, key=lambda name: sum(student[name])/ len(student[name]))
    print("The top scorer is:", Top_scorer)

    Bottom_scorer = min(student, key=lambda name: sum(student[name]) / len(student[name]))
    print("The bottom scorer is:", Bottom_scorer)

    all_grades = [grade for grades in student.values() for grade in grades]
    class_average = sum(all_grades) / len(all_grades)
    print("the class average is:", class_average)
    exit()

student_grades = input("Enter the student's name to view grades:")
print("grades of", student_grades, "are:", student.get(student_grades, "Student not found"))
    
