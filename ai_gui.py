
from copy import deepcopy
import sys
import time

import pygame
from button_choice import ButtonChoice
from correspondance import indice_correspondance
from player_gui import Player_Gui
import PygameUtils as pu


class AIGui(Player_Gui):
    
    def __init__(self, pl, first_player, start):
        super().__init__(pl, first_player, start)
        self.type = "AI"
        if not first_player:
            self.name_1 = pu.button(color="white", x= 480, y=115, width=120, height=50, text="I.A 2", size=30)
            self.level = pu.button(color="white", x= 480, y=150, width=120, height=50, text="Level : "+pl.level, size=25)
        else:
            self.name_1 = pu.button(color="white", x= 480, y=500, width=120, height=50, text="I.A 1", size=30)
            self.level = pu.button(color="white", x= 480, y=535, width=120, height=50, text="Level : "+pl.level, size=25)
        
        if start:
            self.tr = pygame.image.load("images/green_tr.png")
        else:
            self.tr = pygame.image.load("images/red_tr.png")

        self.state_begin = True
        self.begining = ButtonChoice(image=None, pos=(250,330), text_input="Toucher ici pour commencer", size=10, base_color="red", hovering_color="blue")
        

    def new_board_status(self):
        self.b = []
        self.b_opp = []
        for i in range(8):
            self.b.append(self.stones[i].number_stones)
            self.b_opp.append(self.opponent.stones[i].number_stones)

        self.player.set_board(self.b)
        self.player.opponent.set_board(self.b_opp)

    def move_gui_2(self, event, screen, funct, tab_circle, quit_funct):
        print("ENTER AI MOVE")

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        self.tr = pygame.image.load("images/green_tr.png")

        self.new_board_status()
        """print("NEW BOARD STATUS = ", self.player.board)
        print("NEW BOARD STATUS  OPPONENT= ", self.player.opponent.board)"""

        c = self.player.choose_move()

        pos_coor = indice_correspondance(c, self.is_player_1)

        for crl in tab_circle:
            if ((crl.x == pos_coor.x - 5) and (crl.y == pos_coor.y - 5)):
                crl.color = "red"

        time.sleep(1)
        self.semer_gui_1(c, screen, funct, tab_circle)
            
        for crl in tab_circle:
            crl.color = "black"

        self.tr = pygame.image.load("images/red_tr.png")
        self.opponent.tr = pygame.image.load("images/green_tr.png")
        
        if self.opponent.type == "AI":
            if self.game_ov():
                return
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

                    if self.test_2:
                        self.opponent.move_gui(event, screen, funct, tab_circle, quit_funct)
        
        else:
            if self.game_ov():
                return
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
                                
                                pygame.quit()
                                sys.exit()
                            
                            elif self.is_player_1 and event2.pos[1] > 350:
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEMOTION)
                                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)

                            elif not self.is_player_1 and event2.pos[1] < 350:
                                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                                pygame.event.set_blocked(pygame.MOUSEMOTION)
                                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
                                
                            elif self.test_2:
                                self.opponent.move_gui(event2, screen, funct, tab_circle, quit_funct)

    def move_gui(self, event, screen, funct, tab_circle, quit_funct):    
        self.move_gui_2(event, screen, funct, tab_circle, quit_funct)
        
        


        

