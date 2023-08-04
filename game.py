from player import *
from ai import *

player_1 = Player(True)
player_2 = AI(False)
player_1.set_opponent(player_2)
player_2.set_opponent(player_1)
player_2.set_level("EASY")

def jouer(first_player, second_player):

    first_player.move()
        
    print("-----------après 1----------")
   
    print("board_P1 : ", first_player.board)

    print("board_P2 : ", second_player.board)

    second_player.move()

    print("-----------après 2-----------")
    print("board_P1 : ", first_player.board)
    print("board_P2 : ", second_player.board)


def game_over(board):
    game = False
    for i in board:
        if(i == 0):
            game = True    
        else:
            game = False
            break

    return game
    
def partie(P1, P2):
    while not (game_over(P1.board) or game_over(P2.board)):
        jouer(P1,P2)
    print("fin de la partie!!!")

partie(player_1, player_2)

