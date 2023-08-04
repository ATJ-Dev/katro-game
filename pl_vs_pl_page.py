
import sys
import pygame
import PygameUtils as pu

from button_choice import ButtonChoice
from game_gui import Game_Gui
from player import Player
from player_gui import Player_Gui

def get_font(size):
        return pygame.font.Font("assets/font.ttf", size)

class PlVSPlPage:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.title =  ButtonChoice(image=None, pos=(295,70), text_input="Player VS Player", size=25, base_color="yellow", hovering_color="Green")
        self.btn_first_move = pu.button(color="grey", x= 100, y=150, width=95, height=50, text="Joueur qui commence: ", size=30)
        self.btn_pl_dir = pu.button(color="grey", x=100, y= 350, width=95, height=50, text="Sens du premier joueur : ", size=30)
        self.btn_clock = pu.checkbox(
            color="black",
            x=120,
            y=400,
            width=20,
            height=20,
            check=True,
            text="Sens de la montre",
            size=25
        )
        self.btn_anti_clock = pu.checkbox(
            color="black",
            x=120,
            y=450,
            width=20,
            height=20,
            text="Sens contraire à la montre",
            size=25
        )
        self.btn_first_pl1 = pu.checkbox(
            color="black",
            x=120,
            y=200,
            width=20,
            height=20,
            check=True,
            text="Joueur 1",
            size=25
        )
        self.btn_first_pl2 = pu.checkbox(
            color="black",
            x=120,
            y=250,
            width=20,
            height=20,
            text="Joueur 2",
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

    def handling_event(self):
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

                    pl_sens = self.checkbox_choice(sens_choice, "Sens contraire à la montre")
                    pl_start = self.checkbox_choice(first_move_choice, "Joueur 1")

                    if pl_start: 
                        p1 = Player(pl_sens)
                        p2 = Player(not pl_sens)
                    else:
                        p2 = Player(pl_sens)
                        p1 = Player(not pl_sens)
                    
                    p1.set_opponent(p2)
                    p2.set_opponent(p1)

                    pl1 = Player_Gui(p1, True, pl_start)
                    pl2 = Player_Gui(p2, False, not pl_start)

                    pl1.set_opponent_pl_gui(pl2)
                    pl2.set_opponent_pl_gui(pl1)

                    pvp = Game_Gui(self.screen, pl1, pl2)
                    pvp.run()

                for sens in sens_choice:
                    if sens.isOver(mouse_pos):
                        sens.check = True
                        for other in sens_choice:
                            if other != sens:
                                other.check = False

                for fmove in first_move_choice:
                    if fmove.isOver(mouse_pos):
                        fmove.check = True
                        for other in first_move_choice:
                            if other != fmove:
                                other.check = False


    def display(self):
        self.screen.fill("grey")
        self.btn_pl_dir.draw(self.screen)
        self.btn_clock.draw(self.screen)
        self.btn_anti_clock.draw(self.screen)
        self.btn_first_move.draw(self.screen)
        self.btn_first_pl1.draw(self.screen)
        self.btn_first_pl2.draw(self.screen)
        self.btn_back.update(self.screen)
        self.btn_play.update(self.screen)
        self.title.update(self.screen)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.display()
            self.clock.tick(60)


