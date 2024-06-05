import random
import sys
from enum import Enum;

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

gameCount = 0
playerWin = 0
pythonWin = 0

def playRPS():
    playerChoice = int(input('Enter... \n1 For Rock,\n2 For Paper,\n3 For Scissor \n\n'))
    pythonChoise = int(random.choice('123'))


    if(playerChoice not in [1,2,3]):
        print('Please give input from 1 to 3')
        playRPS()

    print('Player Selection: '+str(RPS(playerChoice)).replace('RPS.',''))
    print('Python Selection: '+str(RPS(pythonChoise)).replace('RPS.',''))
    
    def checkWinner():
        global playerWin
        global pythonWin
        if(
            (playerChoice == RPS.ROCK.value and pythonChoise == RPS.SCISSOR.value) or 
            (playerChoice == RPS.SCISSOR.value and pythonChoise == RPS.PAPER.value) or 
            (playerChoice == RPS.PAPER.value and pythonChoise == RPS.ROCK.value)
        ):
            playerWin += 1
            return 'Player win'
        elif(playerChoice == pythonChoise):
            return 'Tie game'
        else:
            pythonWin += 1
            return 'Python win'
        
    rpsResult = checkWinner()
    print(rpsResult)

    global gameCount
    gameCount += 1 

    print("Game Count: "+str(gameCount))
    print("Player Win: "+str(playerWin))
    print("Python Win: "+str(pythonWin))

    while(True):
        playAgain = input('\nWant to continue game?\nY for yes.\nN for no\n')
        if(playAgain.lower() in 'yn'):
            if(playAgain.lower() == 'y'):
                playRPS()
            break      

playRPS()