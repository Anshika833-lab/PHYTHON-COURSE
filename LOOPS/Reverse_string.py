string =input("please enter your own string: ")

#first way
string2 = ("")
for i in string:
    string2 = i + string2
print("\nThe original string =", string)
print("\nThe reversed string =", string2)

#Other way
print("the reversed string =",string[::-1])