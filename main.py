import random
# SNAKE,WATER AND GUN GAME
def gameWIN(you,comp):
    if comp==you:
        return None
    elif comp=='s':
        if you== 'w':
            return False
        elif you== 'g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you== 's':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True    
    

print('Comp Turn : Snake (s), Water (w) or Gun (g)?')

randNo= random.randint(1,3)

if randNo == 1:
    comp='s'

elif randNo == 2:
    comp='w'

elif randNo== 3:
    comp='g'

you= input('YOUR Turn : Snake (s), Water (w) or Gun (g)?')

result = gameWIN(you,comp)

print(f'comp chose {comp}')
print(f'you chose {you}')

if result== None:
    print('IT IS TIE')
elif result == True:
    print('YOU WIN')
else:
    print('YOU LOSE') 


