
from copy import deepcopy

INFINITY = 1.0e400

class Player:
    
    def __init__(self, sens):
        self.sens = sens
        self.board = [2,2,2,2,2,2,2,2]

    def set_board(self, board):
        self.board = board

    def set_opponent(self, opp):
        self.opponent = opp

    def board_status(self):
        return [self.board, self.opponent.board]

    def suivant_case(self, cup):
        if cup == 0:
            return 7
        else:
            return cup - 1

    def prec_case(self, cup):
        if cup == 7:
            return 0
        else:
            return cup + 1

    def rotate_sens(self, cup, sens):
        if (sens == True):
            return self.suivant_case(cup)
        elif (sens == False):
            return self.prec_case(cup)

    def prise(self, cup):
        if cup == 0:
            return 3
        elif cup == 1:
            return 2
        elif cup == 2:
            return 1
        elif cup == 3:
            return 0

    def last_case(self, cup, sens, board):
        temp = cup
        for i in range(board[cup]):
            #last = suivant_case(temp)
            last = self.rotate_sens(temp, sens)
            temp = last
    
        return temp

    def test_first_range(self, case):
        if (case[0]==case[1]==case[2]==case[3]==0):
            return True
        else:
            return False

    def cup_to_take(self, cup, opponent):
        if(self.test_first_range(opponent) == True):
            return cup + 4
        else:
            return self.prise(cup)

    def new_prendre(self, cup, player, opponent):
        print("cup ==== ",cup)
        if (self.test_first_range(opponent) == True):
            player[cup] += opponent[cup + 4]
            opponent[cup + 4] = 0    
        elif (self.test_first_range(opponent) == False): 
            player[cup] += opponent[self.prise(cup)]
            opponent[self.prise(cup)] = 0

    def move(self):
        while True:
            print("Player 1's turn : ")
            c_1 = input("Case pour P1 : ")
            c_1 = int(c_1)
            if self.board[c_1] == 0:
                print("choose another case")
            else:
                self.semer_gui(c_1)
                print("Player status after P1 move: ", self.board_status()[0])
                break

    def semer(self, cup):
        last = self.last_case(cup, self.sens, self.board)
        print("Cup to share = ", cup)
        print("last case = ", last)
        temp = self.rotate_sens(cup, self.sens)
        iter = self.board[cup]
        self.board[cup] = 0
        for i in range(iter):
            self.board[temp] += 1
            temp = self.rotate_sens(temp, self.sens)


        print("board_P1_semer : ", self.board)

        print("board_P2_semer : ", self.opponent.board)
    
        if ((last < 4) and (self.board[last] != 1) ):
            self.new_prendre(last, self.board, self.opponent.board)

        if self.board[last] != 1:
            self.semer(last)

    def semer_gui(self, cup, screen):
        last = self.last_case(cup, self.sens, self.board)
        print("Cup to share = ", cup)
        print("last case = ", last)
        temp = self.rotate_sens(cup, self.sens)
        iter = self.board[cup]
        self.board[cup] = 0
        while iter > 0:
            self.board[temp] += 1
            temp = self.rotate_sens(temp, self.sens)
            iter -= 1
            
        if ((last < 4) and (self.board[last] != 1) ):
            self.new_prendre(last, self.board, self.opponent.board)

        if self.board[last] != 1:
            self.semer_gui(last)

    def game_over(self, board):
        game = False
        for i in board:
            if(i == 0):
                game = True    
            else:
                game = False
                break

        return game
    
    def legal_move(self, board):
        list_legal_move = []
        for i in range(len(board)):
            if (board[i] != 0):
                list_legal_move.append(i)
        return list_legal_move

    def heuristic_eval(self, node):
        nbr_stones_1 = 0
        nbr_stones_2 = 0
        for i in range(len(node[0])):
            nbr_stones_1 += node[0][i]
            nbr_stones_2 += node[1][i]

        return nbr_stones_1 - nbr_stones_2