import random
rand = random.randint(1, 5)
print("****WELCOME TO OUR GAME SECTION****")
Chances = 0

while Chances<=10:
    user = int(input("Enter the number:\n"))
    if(rand>user):
        print("Higer number please")
        Chances+=1

    elif(rand<user):
        print("Lower number please")
        Chances+=1
    else:
        print("You win the game")
        print(f"In {Chances+1} Chances :-) Congrulation!!")
        break

if (rand>user or rand<user):
    print("YOU LOSE THE GAME :-(")
    print(f"Number is {rand}")