import pygame
from ai_vs_ai_page import AiVSAiPage
from button_choice import ButtonChoice
from pl_vs_pl_page import PlVSPlPage
from pl_vs_ai_page import PlVSAiPage



class FirstPage:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.katro_title = ButtonChoice(image=None, pos=(250,180), text_input="KATR", size=55, base_color="black", hovering_color="Green")
        self.picture_stone = pygame.image.load("images/stone_title.png")
        self.picture_stone = pygame.transform.scale(self.picture_stone, (125, 125))
        self.pl_vs_pl_btn = ButtonChoice(image=None, pos=(270,350), text_input="JOUEUR VS JOUEUR", size=20, base_color="yellow", hovering_color="Green")
        self.pl_vs_ai_btn = ButtonChoice(image=None, pos=(270,425), text_input="JOUEUR VS I.A", size=20, base_color="blue", hovering_color="Green")
        self.ai_vs_ai_btn = ButtonChoice(image=None, pos=(270,500), text_input="I.A VS I.A", size=20, base_color="brown", hovering_color="Green")
        

    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("assets/font.ttf", size)
    
    def button_choice(self, pos, text):
        return ButtonChoice(image=None, pos=pos, text_input=text, font=self.get_font(25), base_color="White", hovering_color="Green")

    def handling_event(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for button in [self.pl_vs_pl_btn,self.pl_vs_ai_btn, self.ai_vs_ai_btn]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                print("pos", mouse_pos)
                if self.pl_vs_pl_btn.checkForInput(mouse_pos):
                    PlVSPlPage(self.screen).run()
                
                if self.pl_vs_ai_btn.checkForInput(mouse_pos):
                    PlVSAiPage(self.screen).run()

                if self.ai_vs_ai_btn.checkForInput(mouse_pos):
                    AiVSAiPage(self.screen).run()

                
    def update(self):
        self.stones.move(self.stones.image_correspondance(self.stones), self.stones.x, self.stones.y)

    def display(self):
        self.screen.fill("grey")
        self.katro_title.update(screen=screen)
        self.pl_vs_pl_btn.update(screen=screen)
        self.pl_vs_ai_btn.update(screen=screen)
        self.ai_vs_ai_btn.update(screen=screen)
        screen.blit(self.picture_stone, (345,105))


        pygame.display.flip()

    def run(self):
        while self.running:
            self.handling_event()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((600,700))
first_page_gui = FirstPage(screen)
first_page_gui.run()