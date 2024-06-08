import random
import sys
from enum import Enum;

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


def rps(player):
    gameCount = 0
    playerWin = 0
    pythonWin = 0


    def play():
        playerChoice = int(input(f'{player}, enter... \n1 For Rock,\n2 For Paper,\n3 For Scissor \n\n'))
        pythonChoise = int(random.choice('123'))


        if(playerChoice not in [1,2,3]):
            print('Please give input from 1 to 3')
            play()

        print(f"Player Selection: {str(RPS(playerChoice)).replace('RPS.','')}")
        print(f"Python Selection: {str(RPS(pythonChoise)).replace('RPS.','')}")
        
        def checkWinner():
            nonlocal playerWin
            nonlocal pythonWin
            if(
                (playerChoice == RPS.ROCK.value and pythonChoise == RPS.SCISSOR.value) or 
                (playerChoice == RPS.SCISSOR.value and pythonChoise == RPS.PAPER.value) or 
                (playerChoice == RPS.PAPER.value and pythonChoise == RPS.ROCK.value)
            ):
                playerWin += 1
                return f'{player} win'
            elif(playerChoice == pythonChoise):
                return f'Tie game, Great game {player}.'
            else:
                pythonWin += 1
                return f'Python win, Sorry {player}'
            
        rpsResult = checkWinner()
        print(f"\n*********************\n{rpsResult}\n*********************")

        nonlocal gameCount
        gameCount += 1 

        print(f"Game Count: {gameCount}")
        print(f"{player} Win Count: {playerWin}")
        print(f"Python Win Count: {pythonWin}")

        while(True):
            playAgain = input(f'\nWant to continue game {player}?\nY for yes.\nN for no\n')
            if(playAgain.lower() in 'yn'):
                if(playAgain.lower() == 'y'):
                    play()
                break      
    
    return play


if __name__ == '__main__':
    import argparse

    parse = argparse.ArgumentParser(description="Provides a personal game playing experience.")

    parse.add_argument("-n","--name",dest='name',required=True,help="Name of the player")

    args = parse.parse_args()
    playRPS = rps(args.name)
    playRPS()