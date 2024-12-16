import random as rd
import numpy as np

print('Welcome to Rock-Paper-Scissors, a fun game against the computer!\n')
print('''Rules:
1. In every round, both the computer will choose from either rock, paper or scissors.
2. A point will be awarded to the one who wins the round.
3. The point system is as follows:
    a. Scissors can cut through the paper, so scissors wins against paper.
    b. Paper can wrap up the rock, so paper wins against rock.
    c. Rock can break the scissors, so rock wins over scissors.
4. The first one to score 10 points wins the game.''')

cpoint=0
ppoint=0
arr=np.array([[0,-1,1],[1,0,-1],[-1,1,0]])
opt=['R','P','S']
cont=''

while True:
    for i in range(1,9999):
        print(f'\nRound {i}')
        print('\nType R for rock, P for paper, and S for scissors')
        r1=rd.randint(0,2)
        ncomp=opt[r1]
        while True:
            n=input('Choose an option: ')
            if n.upper() not in opt:
                print('\nPlease choose a correct option.\n')
                continue
            else:
                if n.upper()=='R':
                    print('\nYou choose rock.')
                elif n.upper()=='P':
                    print('\nYou choose paper.')
                else:
                    print('\nYou choose scissors.')
                break
        if ncomp.upper()=='R':
            print('Computer choose rock.')
        elif ncomp.upper()=='P':
            print('Computer choose paper.')
        else:
            print('Computer choose scissors.')

        f=opt.index(n.upper())
        final=arr[f,r1]
        if final==0:
            print('\nBoth pulled out the same choice.\nNo points awarded.')
        elif final==1:
            print('\nYou win this round!\nOne point awarded to you.')
            ppoint+=1
        else:
            print('\nComputer win this round!\nOne point awarded to computer.')
            cpoint+=1

        print('\nYour Points:',ppoint)
        print('Computer Points:',cpoint)

        if cpoint==10 or ppoint==10:
            if cpoint==10:
                print('\nComputer has won the game.')
            else:
                print('\nCongratualtions, You have won the game!')
            cont=input('\nDo you want to play again?(Y for yes, any other key for no): ')
            break

    
    if cont.upper()!='Y':
        print('Thank you for playing the game!')
        break
