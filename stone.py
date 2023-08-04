import pygame
import time

#from correspondance import image_correspondance

class Stone:
    def __init__(self, x, y):
        self.speed = 5
        self.x = x
        self.y = y
        self.number_stones = 2
        self.rect = self.image_correspondance().get_rect(x=x, y=y)


    def image_correspondance(self):
        for i in range(0,17):
            if self.number_stones == i:
                picture = pygame.image.load("images/"+str(i)+".png")
                picture = pygame.transform.scale(picture, (50, 50))
                return picture

    def set_number_stones(self, num):
        self.number_stones = num

    def rect_image(self):
        return self.image_correspondance().get_rect(x=self.x, y=self.y)

    def draw(self, screen):
        screen.blit(self.image_correspondance(), (self.x, self.y))

    def move_right(self, screen, funct):
        i = 0
        while i < 10:
            self.x += 10
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_left(self, screen, funct):
        i = 0
        while i < 10:
            self.x -= 10
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_up(self, screen, funct):
        i = 0
        while i < 10:
            self.y -= 12.5
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_down(self, screen, funct):
        i = 0
        while i < 10:
            self.y += 12.5
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1
        
    def move_take_down_1(self, screen, funct):
        i = 0
        while i < 10:
            self.y += 22.5
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_take_down_2(self, screen, funct):
        i = 0
        while i < 10:
            self.y += 35
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_take_up_1(self, screen, funct):
        i = 0
        while i < 10:
            self.y -= 22.5
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def move_take_up_2(self, screen, funct):
        i = 0
        while i < 10:
            self.y -= 35
            self.draw(screen)
            funct()
            time.sleep(0.1)
            i += 1

    def vertical_move(self, sens, screen, funct):
        pass

    def one_move(self, sens,  screen, funct):
        if not sens:
            #Clock
            if self.y > 350:
                #Pl 1
                if self.x < 360 and self.y < 500:
                    self.move_right(screen, funct)
                elif self.x >= 360 and self.y < 500:
                    self.move_down(screen, funct)
                elif self.x > 60 and self.y > 500:
                    self.move_left(screen ,funct)
                elif self.x <= 60 and self.y > 500:
                    self.move_up(screen, funct)
            elif self.y < 350:
                #Pl 2
                if self.x < 360 and self.y < 100:
                    self.move_right(screen, funct)
                elif self.x >= 360 and self.y < 100:
                    self.move_down(screen, funct)
                elif self.x > 60 and self.y > 100:
                    self.move_left(screen, funct)
                elif self.x <= 60 and self.y > 100:
                    self.move_up(screen, funct)
        else:
            # Anti clock
            if self.y < 350:
                if self.x > 60 and self.y < 100:
                    self.move_left(screen, funct)
                
                elif self.x <= 60 and self.y < 100:
                    self.move_down(screen, funct)

                elif self.x < 360 and self.y > 100:
                    self.move_right(screen, funct)
                
                elif self.x >= 360 and self.y > 100:
                    self.move_up(screen, funct)
            
            elif self.y > 350:
                if self.x > 60 and self.y < 500:
                    self.move_left(screen, funct)
                elif self.x >= 360 and self.y > 500:
                    self.move_up(screen, funct)
                elif self.x >= 60 and self.y > 500:
                    self.move_right(screen ,funct)
                elif self.x <= 60 and self.y < 500:
                    self.move_down(screen, funct)
            
    
    def prendre_move(self, cup_to_take, screen, funct, is_player_1):
        if is_player_1:
            if cup_to_take < 4:
                self.move_take_up_1(screen, funct)
            else:
                self.move_take_up_2(screen, funct)
        
        else:
            if cup_to_take < 4:
                self.move_take_down_1(screen, funct)
            else:
                self.move_take_down_2(screen, funct)

        

                    

