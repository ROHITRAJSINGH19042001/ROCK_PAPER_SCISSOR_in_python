import random

def game(a , b):
    if b == a:
        print("The game is tie.")
    elif b == 'r':
        if a == 'p':
            print("You win!")
        else:
            print("You lose!")
    elif b == 'p':
        if a == 's':
            print("You win!")
        else:
            print("You lose!")
    elif b == 's':
        if a == 'r':
            print("You win!")
        else:
            print("You lose!")                

you = input("Your turn: Rock(r) , Paper(p) , Scissor(s)? ")
print("Computer turn: Rock(r) , Paper(p) , Scissor(s)?")
r = random.randint(1,3)
print("Compter Selected:",r)
if r == 1 :
    computer = 'r'
elif r == 2 :
    computer = 'p'
elif r == 3 :
    computer = 's'
game(you , computer)