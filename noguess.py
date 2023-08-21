def guess():
    i=1
    found=0
    print("You can made ten guesses")
    while(i<=10):
        print("Enter your ",i,"guess")
        inputno=int(input())
        if(random==inputno):
            found=1
            break
        elif(inputno+20 < random):
            print("Your guess is too low")
        elif(inputno < random):
            print("Your guess is low")
        elif(inputno > random+20):
            print("Your guess is too  high")
        elif(inputno > random):
            print("Your guess is  high")
        i+=1
    if(found==1):
        if(i==1):
            marks=100
        elif(i==2):
            marks=90
        elif(i==3):
            marks=80
        elif(i==4):
            marks=70
        elif(i==5):
            marks=60
        if(i==1 or i==2 or i==3 or i==3 or i==4 or i==5):
            print("Hurray!! You scored ",marks,"marks")
    else:
        print("Sorry..Game Over")
import random
print("Welcome to number guessing Game")
random=random.randint(1,100)
guess()

nxt=(input("Do you want to continue (Y/N)"))
if(nxt=="Y"):
    guess()

    
        
