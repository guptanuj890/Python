print("Welcome to the game!")

playing=input('Do you want to play the game? ')

if playing.lower()!='yes':
    quit()
    
print("Let's Play!")
score=0

answer=input('What does CPU stand for? ')

if answer.lower()=='central processing unit':
    print('Correct :)')
    score+=1
else:
    print('Incorrect :(')
    
answer=input('What does GPU stand for? ')

if answer.lower()=='graphics processing unit':
    print('Correct :)')
    score+=1
else:
    print('Incorrect :(') 

print("You got "+ str(score)+' questions correct!')                
