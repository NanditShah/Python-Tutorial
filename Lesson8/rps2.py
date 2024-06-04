import random
import sys
from enum import Enum;

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

playAgain = True

while playAgain:
    playerChoice = int(input('Enter... \n1 For Rock,\n2 For Paper,\n3 For Scissor \n\n'))
    pythonChoise = int(random.choice('123'))


    if(playerChoice not in [1,2,3]):
        sys.exit('Please give input from 1 to 3')

    print('Player Selection: '+str(RPS(playerChoice)).replace('RPS.',''))
    print('Python Selection: '+str(RPS(pythonChoise)).replace('RPS.',''))

    if(
        (playerChoice == RPS.ROCK.value and pythonChoise == RPS.SCISSOR.value) or 
        (playerChoice == RPS.SCISSOR.value and pythonChoise == RPS.PAPER.value) or 
        (playerChoice == RPS.PAPER.value and pythonChoise == RPS.ROCK.value)
    ):
        print('Player win')
    elif(playerChoice == pythonChoise):
        print('Tie game')
    else:
        print('Python win')

    
    while(True):
        playAgain = input('\nWant to continue game?\nY for yes.\nN for no\n')
        if(playAgain.lower() in 'yn'):
            playAgain = playAgain == 'y'            
            break           