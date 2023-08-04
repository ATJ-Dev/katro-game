import sys
import pygame
from button_choice import ButtonChoice

from circles import Circles

class Game_Gui:
    def __init__(self, screen, pl1, pl2):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.area1 = pygame.Rect(35, 50, 400, 225)
        self.area2 = pygame.Rect(35,400, 400,225)
        self.circles = [Circles(55,420,63,63), Circles(155,420,63,63), Circles(255,420,63,63),Circles(355,420,63,63),
        Circles(355,545,63,63), Circles(255,545,63,63), Circles(155,545,63,63), Circles(55,545,63,63),
        Circles(355,195,63,63), Circles(255,195,63,63), Circles(155,195,63,63) ,Circles(55,195,63,63),
        Circles(55,70,63,63), Circles(155,70,63,63) ,Circles(255,70,63,63) ,Circles(355,70,63,63)]
        self.player1 = pl1
        self.player2 = pl2
        if ((pl1.start and not pl1.player.sens) or (pl2.start and pl2.player.sens)):
            self.arrow_pl1_1 = pygame.image.load("images/left_arrow.png")
            self.arrow_pl1_2 = pygame.image.load("images/right_arrow.png")
            self.arrow_pl2_1 = pygame.image.load("images/right_arrow.png")
            self.arrow_pl2_2 = pygame.image.load("images/left_arrow.png")
        elif ((pl1.start and pl1.player.sens) or (pl2.start and not pl2.player.sens)):
            self.arrow_pl1_1 = pygame.image.load("images/right_arrow.png")
            self.arrow_pl1_2 = pygame.image.load("images/left_arrow.png")
            self.arrow_pl2_1 = pygame.image.load("images/left_arrow.png")
            self.arrow_pl2_2 = pygame.image.load("images/right_arrow.png")
        
        self.color_circle = "black"
        self.pl = [self.player1, self.player2]
        self.btn_quit = ButtonChoice(image=None, pos=(550,660), text_input="SORTIR", size=15, base_color="red", hovering_color="black")
        self.game_over_text = ButtonChoice(image=None, pos=(300,320), text_input="GAME OVER", size=25, base_color="black", hovering_color="black")

    def quit_funct(self):
        self.running = False

    def play_game(self):
        self.handling_event()

    def pl1_move(self, event):
        self.player1.move_gui(event, self.screen, self.display, self.circles, self.back_to_back)

    def pl2_move(self, event):
        self.player2.move_gui(event, self.screen, self.display, self.circles, self.back_to_back)

    def turn(self, event, turn):
        if turn:
            if self.player1.type == "AI":
                if self.player1.begining.checkForInput(event.pos):
                    self.player1.state_begin = False
                    self.pl1_move(event)

            if event.pos[1] < 350:
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        
            else:
                self.pl1_move(event)

        else:
            if self.player2.type == "AI":
                if self.player2.begining.checkForInput(event.pos):
                    self.player2.state_begin = False
                    self.pl2_move(event)

            if event.pos[1] > 350 and event.pos[1] < 650:
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_allowed(pygame.MOUSEBUTTONDOWN)
        
            else:
                self.pl2_move(event)

    def game_over(self):
        return True

    def handling_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.player1.btn_quit_pl.checkForInput(event.pos):
                    self.running = False
            
                self.turn(event, self.player1.start)   

    def back_to_back(self):
        print("---------------BACK TO BACK 1-------------------")
        print("RUNNING STATE 1", self.running)
        self.running = False
        print("RUNNING STATE 2", self.running)

        print("---------------BACK TO BACK 2-------------------")
    
    
    def update(self):
        print("---------------UPDATE 1-------------------")
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.btn_quit.checkForInput(event.pos):
                    self.running = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        print("---------------UPDATE 2-------------------")
     

    def display(self):

        self.screen.fill("grey")

        self.player1.tr = pygame.transform.scale(self.player1.tr, (20,20))
        self.player2.tr = pygame.transform.scale(self.player2.tr, (20,20))
        self.screen.blit(self.player1.tr, (450,510))
        self.screen.blit(self.player2.tr, (450,135))


        self.player1.name_1.draw(self.screen)
        self.player2.name_1.draw(self.screen)
        self.player1.level.draw(self.screen)
        self.player2.level.draw(self.screen)

        self.arrow_pl1_1 = pygame.transform.scale(self.arrow_pl1_1, (50, 50))
        self.arrow_pl1_2 = pygame.transform.scale(self.arrow_pl1_2, (50, 50))
        self.arrow_pl2_1 = pygame.transform.scale(self.arrow_pl2_1, (50, 50))
        self.arrow_pl2_2 = pygame.transform.scale(self.arrow_pl2_2, (50, 50))

        pygame.draw.rect(self.screen, "black", self.area1, 5, 10)
        pygame.draw.rect(self.screen, "black", self.area2, 5, 10)

        self.screen.blit(self.arrow_pl1_1, (200, 30))
        self.screen.blit(self.arrow_pl1_2, (200, 250))
        self.screen.blit(self.arrow_pl2_1, (200, 380))
        self.screen.blit(self.arrow_pl2_2, (200, 600))
        
        for st in self.player1.stones:
            st.draw(self.screen)
        
        for st in self.player2.stones:
            st.draw(self.screen)
        
        self.player1.stone_temp.draw(self.screen)
        self.player1.stone_take.draw(self.screen)
        self.player2.stone_temp.draw(self.screen)
        self.player2.stone_take.draw(self.screen)

        for cercle in self.circles: 
            cercle.draw_circle(self.screen)

        self.player1.btn_quit_pl.update(self.screen)

        if self.player1.game_ov() or self.player2.game_ov():
            if self.player1.game_ov():
                self.pl_winner_text = ButtonChoice(image=None, pos=(320,360), text_input="Winner "+ self.player2.name_1.text, size=25, base_color="green", hovering_color="black")
                print("Winner", self.player2.name_1.text)
                
            else:
                self.pl_winner_text = ButtonChoice(image=None, pos=(320,360), text_input="Winner "+ self.player1.name_1.text, size=25, base_color="green", hovering_color="black")
                print("Winner", self.player1.name_1.text)


            self.game_over_text.update(self.screen)
            self.pl_winner_text.update(self.screen)
        
        for pl in [self.player1, self.player2]:
            if pl.type == "AI" and pl.start:
                if pl.state_begin:
                    pl.begining.update(self.screen)
    
        pygame.display.flip()

    def run(self):
        while self.running:
            self.play_game()
            self.update()
            self.display()
            self.clock.tick(60)
