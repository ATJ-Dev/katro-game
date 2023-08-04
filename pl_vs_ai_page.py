
import sys
import pygame
import PygameUtils as pu
from ai import AI
from ai_gui import AIGui

from button_choice import ButtonChoice
from game_gui import Game_Gui
from player import Player
from player_gui import Player_Gui

def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

class PlVSAiPage:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.title =  ButtonChoice(image=None, pos=(295,70), text_input="JOUEUR VS I.A", size=25, base_color="blue", hovering_color="Green")

        self.ai_level_btn = pu.button(color="white", x= 75, y=150, width=50, height=0, text="Niveau de l' I.A : ", size=30)
        self.easy_btn = pu.checkbox(
            color="black",
            x=75,
            y=175,
            width=15,
            height=15,
            check=True,
            text="EASY",
            size=25
        )
        self.medium_btn = pu.checkbox(
            color="black",
            x=200,
            y=175,
            width=15,
            height=15,
            text="MEDIUM",
            size=25
        )
        self.hard_btn = pu.checkbox(
            color="black",
            x=325,
            y=175,
            width=15,
            height=15,
            text="HARD",
            size=25
        )
        self.btn_first_move = pu.button(color="white", x=100, y= 320, width=50, height=0, text="Joueur qui commence : ", size=30)
        self.btn_first_pl1 = pu.checkbox(
            color="black",
            x=75,
            y=350,
            width=15,
            height=15,
            check=True,
            text="Joueur 1",
            size=25
        )
        self.btn_first_pl2 = pu.checkbox(
            color="black",
            x=75,
            y=380,
            width=15,
            height=15,
            text="I.A",
            size=25
        )
        self.btn_sens = pu.button(color="white", x=75, y= 480, width=120, height=0, text="Sens du premier joueur : ", size=30)
        self.btn_clock = pu.checkbox(
            color="black",
            x=75,
            y=510,
            width=15,
            height=15,
            check=True,
            text="Sens de la montre",
            size=25
        )
        self.btn_anti_clock = pu.checkbox(
            color="black",
            x=75,
            y=540,
            width=15,
            height=15,
            text="Sens contraire à la montre",
            size=25
        )
        self.btn_back = ButtonChoice(image=None, pos=(150, 650), text_input="BACK", size=35, base_color="black", hovering_color="red")
        self.btn_play = ButtonChoice(image=None, pos=(375, 650), text_input="PLAY", size=35, base_color="black", hovering_color="green")

    def checkbox_choice(self, tab, text):
        for choice in tab:
            if choice.check == True:
                if choice.text == text:
                    return True
                else:
                    return False

    def checkbox_case(self, tab, pos):
        for iter in tab:
            if iter.isOver(pos):
                iter.check = True
                for other in tab:
                    if other != iter:
                        other.check = False

    def level_choice(self, tab):
        for iter in tab:
            if iter.check == True:
                return iter.text


    def handling_event(self):
        level_choice = [self.easy_btn, self.medium_btn, self.hard_btn]
        sens_choice = [self.btn_clock, self.btn_anti_clock]
        first_move_choice = [self.btn_first_pl1, self.btn_first_pl2]
        choices = [self.btn_back, self.btn_play]
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        for button in choices:
            button.changeColor(MENU_MOUSE_POS)
            button.update(self.screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if self.btn_back.checkForInput(mouse_pos):
                    self.running = False
                
                if self.btn_play.checkForInput(mouse_pos):
                    """-------------READY TO PLAY--------------"""
                    pl_sens = self.checkbox_choice(sens_choice, "Sens contraire à la montre")
                    pl_start = self.checkbox_choice(first_move_choice, "Joueur 1")
                    ai_level = self.level_choice(level_choice)

                    print("Choix du niveau = ", ai_level)
                    print("------------PL START--------------------", pl_start)
                    if pl_start:
                        p1 = Player(pl_sens)
                        p2 = AI(not pl_sens)
                    else:
                        p2 = AI(pl_sens)
                        p1 = Player(not pl_sens)

                    p1.set_opponent(p2)
                    p2.set_opponent(p1)
                    
                    p2.set_level(ai_level)

                    pl1 = Player_Gui(p1, True, pl_start)
                    pl2 = AIGui(p2, False, not pl_start)

                    pl1.set_opponent_pl_gui(pl2)
                    pl2.set_opponent_pl_gui(pl1)

                    print("Choix du niveau 2 = ", pl2.player.level)
                    
                    pva = Game_Gui(self.screen, pl1, pl2)
                    pva.run()

                self.checkbox_case(level_choice, mouse_pos)
                self.checkbox_case(first_move_choice, mouse_pos)
                self.checkbox_case(sens_choice, mouse_pos)



    def display(self):
        self.screen.fill("grey")
        self.title.update(self.screen)
        self.ai_level_btn.draw(self.screen)
        self.easy_btn.draw(self.screen)
        self.medium_btn.draw(self.screen)
        self.hard_btn.draw(self.screen)

        self.btn_sens.draw(self.screen)
        self.btn_clock.draw(self.screen)
        self.btn_anti_clock.draw(self.screen)
        

        self.btn_first_move.draw(self.screen)
        self.btn_first_pl1.draw(self.screen)
        self.btn_first_pl2.draw(self.screen)
        self.btn_back.update(self.screen)
        self.btn_play.update(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.display()
            self.clock.tick(60)


