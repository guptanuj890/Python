import random

user_wins=0
comp_wins=0

options=['rock','paper','scissor']

while True:
    user_input=input("Type Rock/Paper/Scissor or press Q to quit: ")
    user_input=user_input.lower()
    if user_input=='q':
        break
    if user_input not in ['rock','paper','scissor']:
        continue
    
    random_number=random.randint(0,2) # rock:0,paper:1,scissor:2
    computer_pick=options[random_number]
    print('Computer Picked ')
    
    if user_input==computer_pick:
        print('Tied')
    elif user_input=='rock' and computer_pick=='scissor':
        print('You Win ')
        user_wins+=1
    elif user_input=='paper' and computer_pick=='rock':
        print('You Win ')
        user_wins+=1
    elif user_input=='scissor' and computer_pick=='paper':
        print('You Win ')
        user_wins+=1            
    else:
        print('Computer Wins ')
        comp_wins+=1
print("You won",user_wins,"times.")
print("Computer wins",comp_wins,"times.")
print("GoodBye")            