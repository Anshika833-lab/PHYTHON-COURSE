print("enter marks obtained in 4 subjects: ")
math = int(input("maths:"))
english = int(input("english:"))
science = int(input("Science:"))
hindi = int(input("hindi:"))

sum= math+science+english+hindi
print("sum of math,science,english and hindi:", sum)
perc = (sum/400)*100
print("percentage mark=", perc)