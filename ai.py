import random
from player import *


class AI(Player):
    
    def __init__(self, sens):
        super().__init__(sens)


    def set_level(self, level):
        self.level = level

    def choose_move(self):
        if self.level == "EASY":
            c = self.random_move()
        elif self.level == "MEDIUM":
            c, score = self.mini_max(self.board_status(), True, 1)
        elif self.level == "HARD":
            c, score = self.mini_max(self.board_status(), True, 2)
        
        return c

    def move(self):
        print("AI's turn : ")
        temp = deepcopy(self.board_status())
        c_2 = self.choose_move()
        print("AI's move = ", c_2)
        self.set_board(temp[0])
        self.opponent.set_board(temp[1])
        print("Player status before P2 move: ", self.board_status())
        self.semer_gui(c_2)
        print("Player status after P2 move: ", self.board_status()[1])

        
    def random_move(self):
        legal_move = self.legal_move(self.board)
        choice = random.choice(legal_move)
        return choice

    def mini_max(self, node, player, depth):
        print("Enter on MINIMAX with depth === ", depth)
        
        if (self.game_over(node[0]) or self.game_over(node[1]) or depth == 0):
            print("///////////////////////////")
            print("heuristic val === ", self.heuristic_eval(node))
            print("///////////////////////////")
            return 0, self.heuristic_eval(node)
        
        elif player == True:
            print("***************")
            print("Player MAX == ")
            print("***************")
            print("legal move = ", self.legal_move(node[0]))
            pl_1 = Player(self.sens)
            pl_2 = Player(not self.sens)
            pl_1.set_opponent(pl_2)
            pl_2.set_opponent(pl_1)
            pl_1.set_board(node[0])
            pl_2.set_board(node[1])
            val = - INFINITY
            node_temp = deepcopy(node)
            for i in self.legal_move(node[0]):
                pl_1.set_board(node[0])
                pl_2.set_board(node[1])
                print("for i MAX in legal move i = ", i)
                pl_1.semer(i)
                node_1 = [pl_1.board, pl_2.board]
                temp_choice, temp_score = self.mini_max(node_1, False, depth - 1)
                if val < temp_score:
                    choice = i
                    val = temp_score
                node = deepcopy(node_temp)
            print("vallMax = ", val, "indice == ",choice)
            return choice, val

        elif player == False:
            print("***************")
            print("Player MIN == ")
            print("***************")
            pl_1 = Player(self.sens)
            pl_2 = Player(not self.sens)
            pl_1.set_opponent(pl_2)
            pl_2.set_opponent(pl_1)
            pl_1.set_board(node[0])
            pl_2.set_board(node[1])
            val = INFINITY
            temp_b = deepcopy(node)
            print("legal move = ", self.legal_move(node[1]))
            for i in self.legal_move(node[1]):
                pl_1.set_board(node[0])
                pl_2.set_board(node[1])
                print("for i MIN in legal move i = ", i)
                pl_2.semer(i)
                node_1 = [pl_1.board, pl_2.board]
                temp_choice, temp_val = self.mini_max(node_1, True, depth - 1)
                if val > temp_val:
                    choice = i
                    val = temp_val
                node = deepcopy(temp_b)
            print("valllMin = ", val, "indice == ",choice)
            return choice, val



