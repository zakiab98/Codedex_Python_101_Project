import random

computerp=0
playerp=0

while computerp <3 and playerp <3:

    print("====================")
    print("Rock Paper Scissors")
    print("The first to have 3 points win!")
    print("====================")
    print("1)✊\n2)✋\n3)✌️")

    computer = random.randint(1,3)
    player = (int(input("Pick a number:")))

    if(player ==1 and computer ==1):
        print("you chose :✊ \n CPU chose :✊ \n it's a draw! You each get 1 points ")
        computerp+=1
        playerp+=1
    elif(player==1 and computer==2):
        print("you chose :✊ \n CPU chose :✋ \n  ")
        computerp+=1
    elif(player==1 and computer==3):
        print("you chose :✊ \n CPU chose :✌️ \n  ")
        playerp+=1
    elif(player ==2 and computer ==2):
        print("you chose :✋ \n CPU chose :✋ \n it's a draw! You each get 1 points ")
        computerp+=1
        playerp+=1
    elif(player==2 and computer==1):
        print("you chose :✋ \n CPU chose :✊ \n ")
        playerp+=1
    elif(player==2 and computer==3):
        print("you chose :✋ \n CPU chose :✌️ \n ")
        computerp+=1
    elif(player ==3 and computer ==3):
        print("you chose :✌️ \n CPU chose :✌️ \n it's a draw! You each get 1 points ")
        computerp+=1
        playerp+=1
    elif(player==3 and computer==1):
        print("you chose :✌️ \n CPU chose :✊ \n  ")
        computerp+=1
    else:
        print("you chose :✌️ \n CPU chose :✋ \n  ")
        playerp+=1

    print(f'The player has {playerp} points and the CPU has {computerp} points')

if(playerp==computerp):
    print("You are both winners! congrats!")
elif playerp>computerp:
    print('The player won!')
else:
    print('The CPU won!')


    
    



