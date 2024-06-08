from rps import rps
from guess_my_number import guess_my_number

def arcade(name="Player"):
    while True:
        game = input(f'\nHey {name}.\nWelcome to the arcade.\nSelect 1 to play Rock-Paper-Secissor.\nSelect 2 to play Guess My Number.\n\nOr press "x" to exist from arcade.\n')

        if(game not in ['1','2','x']):
            continue
        else:
            if(game == '1'): 
                rps(name)()
            elif(game == '2'):
                guess_my_number(name)()
            else:
                break

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Provides a personal game playing experience')
    
    parser.add_argument("-n","--name",dest='name',required=True,help='Name of the player')
    args = parser.parse_args()
    arcade(args.name)



