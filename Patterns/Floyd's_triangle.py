print("floyd's triangle:")
n = int(input("enter the number of rows :"))
number = 1

for row in range(n):
    for j in range (1, row+1):
        print(number, end=" ")
        number +=1
    print()