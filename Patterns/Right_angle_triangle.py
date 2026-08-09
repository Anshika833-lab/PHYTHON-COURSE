print("Half pyramid pattern of stars (*):")
n = int(input("enter the number of rows :"))

for row in range(n):
    for j in range (row+1):
        print("*", end="")
    print()


    