print("=====GUESS THE SECRET NUMBER=====")
secret_number = 31

hearts = 5
number =int(input("guess the secret number from 1 to 50:"))

if number >= 20:
    print("warm, close guess!!")
    print('But it is wrong!')
    hearts=4
    print("you have", hearts, "hearts left")
    

elif number <20:
    print("cold, you are far away!")
    print("you are still wrong!")
    hearts =3
    print("you have", hearts, "hearts left")

elif number <10:
    print("ice cold, you are very far away!")
    print("you are still wrong!")
    hearts =2
    print("you have", hearts, "hearts left")

elif number <=30:
    print("HOT, you are almost there!")
    hearts=1
    print("you have", hearts, "hearts left")

elif number == 31:
    print("Congratulations! You guessed the secret number!")
    print("great job!!")

elif number < 40:
    print('warm, close guess!!')
    hearts = 0
    print("you have", hearts, "hearts left")
    print("you have lost the game, better luck next time!")

    if hearts ==0:
        print("you ran out of hearts!!")
    
    
    



    
        


    
    





        
        





 
     
    
