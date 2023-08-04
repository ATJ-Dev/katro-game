
import pygame


def coor_correspondance(x,y):
    if x == 60 and y == 75:
        return 4

    elif x == 160 and y == 75:
        return 5
    
    elif x == 260 and y == 75:
        return 6

    elif x == 360 and y == 75:
        return 7
    
    elif x == 60 and y == 200:
        return 3

    elif x == 160 and y == 200:
        return 2
    
    elif x == 260 and y == 200:
        return 1
    
    elif x == 360 and y == 200:
        return 0

    if x == 60 and y == 425:
        return 0

    elif x == 160 and y == 425:
        return 1
    
    elif x == 260 and y == 425:
        return 2

    elif x == 360 and y == 425:
        return 3
    
    elif x == 60 and y == 550:
        return 7

    elif x == 160 and y == 550:
        return 6
    
    elif x == 260 and y == 550:
        return 5
    
    elif x == 360 and y == 550:
        return 4


            
def indice_correspondance(a, player_1):
    picture_temp = pygame.image.load("images/0.png")
    picture_temp = pygame.transform.scale(picture_temp, (50, 50))

    if player_1:
        if a == 4:
            return picture_temp.get_rect(x=360, y=550)

        elif a == 5:
            return picture_temp.get_rect(x=260, y=550)
    
        elif a == 6:
            return picture_temp.get_rect(x=160, y=550)

        elif a == 7:
            return picture_temp.get_rect(x=60, y=550)
    
        elif a == 3:
            return picture_temp.get_rect(x=360, y=425)

        elif a == 2:
            return picture_temp.get_rect(x=260, y=425)

        elif a == 1:
            return picture_temp.get_rect(x=160, y=425)

        elif a == 0 :
            return picture_temp.get_rect(x=60, y=425)
    
    else:
        if a == 4:
            return picture_temp.get_rect(x=60, y=75)

        elif a == 5:
            return picture_temp.get_rect(x=160, y=75)
    
        elif a == 6:
            return picture_temp.get_rect(x=260, y=75)

        elif a == 7:
            return picture_temp.get_rect(x=360, y=75)
    
        elif a == 3:
            return picture_temp.get_rect(x=60, y=200)

        elif a == 2:
            return picture_temp.get_rect(x=160, y=200)

        elif a == 1:
            return picture_temp.get_rect(x=260, y=200)

        elif a == 0 :
            return picture_temp.get_rect(x=360, y=200)
        
