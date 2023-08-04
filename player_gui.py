import sys
import pygame
from button_choice import ButtonChoice
from correspondance import coor_correspondance, indice_correspondance
import PygameUtils as pu

from stone import Stone

class Player_Gui:
    def __init__(self, pl, is_first_player, start):
        self.type = "Player"
        self.start = start
        if is_first_player:
            self.stones = [Stone(60,425),  Stone(160,425), Stone(260,425), Stone(360,425), Stone(360,550),Stone(260,550),
            Stone(160,550), Stone(60,550)]
        else:
            self.stones = [Stone(360,200), Stone(260,200),Stone(160,200), Stone(60,200), 
             Stone(60,75), Stone(160,75), Stone(260,75), Stone(360,75)]
        self.player = pl
        self.stone_temp = Stone(700,800)
        self.stone_take = Stone(600,800)
        self.is_player_1 = is_first_player
        self.test = True
        self.test_2 = True

        if is_first_player:
            self.name_1 = pu.button(color="white", x= 480, y=500, width=100, height=50, text="PLAYER 1", size=30)
        
        else:
            self.name_1 = pu.button(color="white", x= 480, y=125, width=100, height=50, text="PLAYER 2", size=30)

        if start:
            self.tr = pygame.image.load("images/green_tr.png")
        else:
            self.tr = pygame.image.load("images/red_tr.png")

        self.level = pu.button(color="white", x= 880, y=800, width=0, height=0, text="", size=30)     
        self.btn_quit_pl = ButtonChoice(image=None, pos=(550,660), text_input="SORTIR", size=15, base_color="red", hovering_color="black")



    def update_stones(self):
        for i in range (len(self.player.board)):
            self.stones[i].set_number_stones(self.player.board[i])

    def set_opponent_pl_gui(self, opponent):
        self.opponent = opponent

    def up_to_date(self):
        self.tr = pygame.image.load("images/red_tr.png")
        self.opponent.tr = pygame.image.load("images/green_tr.png")

    def total_move(self, position, screen, funct, tab_circle, event, quit_funct):
        #print("ENTREE TOTAL MOVE")
        
        self.tr = pygame.image.load("images/green_tr.png")

        indice = coor_correspondance(position.x, position.y)
        """print("indice : ", indice)
        print("position : ", position)"""
        pos_coor = indice_correspondance(indice, self.is_player_1)

        for crl in tab_circle:
            if ((crl.x == pos_coor.x - 5) and (crl.y == pos_coor.y - 5)):
                crl.color = "red"
        
        self.semer_gui_1(indice, screen, funct, tab_circle)

        for crl in tab_circle:
            crl.color = "black"
        
        if self.game_ov():
            return
        else:
            if self.opponent.type == "AI":
                for event2 in pygame.event.get():
                    if event2.type == pygame.MOUSEBUTTONDOWN:   
                        if event2.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                            
                        elif self.btn_quit_pl.checkForInput(event2.pos):
                            quit_funct()
                            self.test = False
                            self.test_2 = False
                            break
        
                self.opponent.move_gui(event, screen, funct, tab_circle, quit_funct)

            else:
                while self.test:
                    for event2 in pygame.event.get():

                        if event2.type == pygame.MOUSEBUTTONDOWN:   
                            if event2.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()

                            elif self.btn_quit_pl.checkForInput(event2.pos):
                                quit_funct()
                                self.test = False
                                self.test_2 = False
                                break
                                #pygame.quit()
                                #sys.exit()

                            elif self.is_player_1 and event2.pos[1] > 350: 
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEMOTION)
                                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                
                            elif not self.is_player_1 and event2.pos[1] < 350:
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEMOTION)
                                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                    
                            else:
                                self.opponent.move_gui(event2, screen, funct, tab_circle, quit_funct)
    
    def move_gui(self, event, screen, funct, tab_circle, quit_funct):
        
        print("wait...")        
        
        stone_numbers = []

        for i in range(8):
            stone_numbers.append(self.stones[i].number_stones)

        positions = []
        indices = []
        for l_m in self.legal_move_gui(stone_numbers):
            positions.append(self.stones[l_m].rect_image())
        
        print("---------------------------------------------")
        
        for pos in positions:
            indice = coor_correspondance(pos.x, pos.y)
            indices.append(indice)

        print("Legal move", indices)
        print("---------------------------------------------")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for position in positions:
                if position.collidepoint(event.pos): 
                    self.total_move(position, screen, funct, tab_circle, event, quit_funct)

        print("FIN MOVE GUI")


    def game_ov(self):
        game = False
        stones = []
        for i in range(8):
            stones.append(self.stones[i].number_stones)

        for i in stones:
            if(i == 0):
                game = True    
            else:
                game = False
                break

        return game

    def legal_move_gui(self, board):
        list_legal_move = []
        for i in range(8):
            if (board[i] != 0):
                list_legal_move.append(i)
        return list_legal_move


    def set_stones_gui(self):
        for i in range(8):
            self.stones[i].number_stones = self.player.board[i]

    """---------------------------------------------"""

    def last_case_gui(self, cup, sens):
        temp = cup
        for i in range(self.stones[cup].number_stones):
            
            last = self.player.rotate_sens(temp, sens)
            temp = last
    
        return temp

    def semer_gui_1(self, indice, screen, funct, tab_circle):

        print("-----------ENTER SEMER-------------")
        
        """print("INDICE", indice)
        print("number stones = ", self.stones[indice].number_stones)"""
             
        b_last = self.last_case_gui(indice, self.player.sens)
        b_temp = self.player.rotate_sens(indice, self.player.sens)
        b_iter = self.player.board[indice]
        self.player.board[indice] = 0

        temp = self.player.rotate_sens(indice, self.player.sens)
        self.stone_temp.x = self.stones[indice].x
        self.stone_temp.y = self.stones[indice].y
        print("last case b last = ", b_last)

        self.stone_temp.number_stones = self.stones[indice].number_stones

        """print("number =", self.stones[indice].number_stones)
        print("number temp 0=", self.stone_temp.number_stones)"""

        self.stones[indice].number_stones = 0
        """print("aaa", self.stone_temp.x)
        print("bbb", self.stone_temp.y)
        print("number temp =", self.stone_temp.number_stones)
        print("number 2 =", self.stones[indice].number_stones)"""
        
        while self.stone_temp.number_stones > 0:
            self.player.board[temp] += 1
            b_temp = self.player.rotate_sens(b_temp, self.player.sens)
            self.stone_temp.one_move(self.player.sens, screen, funct)
            self.stone_temp.number_stones -= 1
            self.stones[temp].number_stones += 1
            temp = self.player.rotate_sens(temp, self.player.sens)

        temp_tab_1 = []
        for i in range(4):
            temp_tab_1.append(self.opponent.stones[i].number_stones)

        if ( (b_last < 4) and (self.stones[b_last].number_stones > 1) and (self.opponent.stones[self.player.cup_to_take(b_last, temp_tab_1)].number_stones != 0)):
            temp_tab = []
            for i in range(4):
                temp_tab.append(self.opponent.stones[i].number_stones)

            ctt = self.player.cup_to_take(b_last, temp_tab)
            print("cup to take = ", ctt)
            self.stone_take.x = indice_correspondance(ctt, not self.is_player_1).x
            self.stone_take.y = indice_correspondance(ctt, not self.is_player_1).y
            self.stone_take.number_stones = self.opponent.stones[ctt].number_stones
            self.opponent.stones[ctt].number_stones = 0
            self.stone_take.prendre_move(ctt, screen, funct, not self.is_player_1)
            self.stones[b_last].number_stones += self.stone_take.number_stones
            self.stone_take.number_stones = 0

        #print("temp - 1 =", self.stones[b_last].number_stones)
        
        self.up_to_date()
        
        if self.stones[b_last].number_stones != 1 and (not self.game_ov() or not self.opponent.game_ov()):        
            self.semer_gui_1(b_last, screen, funct, tab_circle)
        

        
        
    