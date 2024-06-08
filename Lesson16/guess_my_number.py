import random
import argparse

def guess_my_number(player):
    player_win = 0
    total_games = 0

    def play():
        nonlocal player_win,total_games

        actualNumber = int(random.choice('123'))

        
        while(True):
            playerAns = int(input(f'\nGuess the number between 1 to 3, {player}\n'))

            if(playerAns not in [1,2,3]):
                continue
            else:
                if(actualNumber == playerAns):
                    print(f'\n{player} you won')
                    player_win+=1
                else:
                    print(f'\nSorry {player}, you lost')
                total_games += 1
                break

        print(f'\n{player} game win count - {player_win}')
        print(f'\nComputer game win count - {total_games - player_win}')
        print(f'\n{player} game win percentage - {(player_win/total_games)*100:.2f}%')
    
    
        while(True):
            playAgain = input(f'\nWant to continue game {player}?\nY for yes.\nN for no\n')
            if(playAgain.lower() in 'yn'):
                if(playAgain.lower() == 'y'):
                    play()
                break
    
    return play

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Provides a personal game playing experience.")

    parser.add_argument('-n','--name',dest='name',required=True,help="Name of the player")

    args = parser.parse_args()
    game = guess_my_number(args.name)
    game()