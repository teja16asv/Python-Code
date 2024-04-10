import random

def gameWin(comp, you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='s':
            return False
        elif you=='p':
            return True    
    elif comp=='p':
        if you=='r':
            return False
        elif you=='s':
            return True
    elif comp=='s':
        if you=='p':
            return False
        elif you=='r':
            return True
        
print("Computer's turn:Rock(r), Paper(p), Scissor(s): ")
randNo=random.randint(1,3)
if randNo==1:
    comp='r'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='s'

you=input("Your turn: Rock(r), Paper(p), Scissor(s): ")
a=gameWin(comp, you)

print("The computer's choice is: ", comp)
print("Your choice is: ", you)
if a==None:
    print("This is a Tie")
elif a:
    print("You Won")
else:
    print("You Lost")