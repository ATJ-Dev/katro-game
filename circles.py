
import pygame


class Circles:
    def __init__(self, x, y, width, height):
        self.circle = pygame.Rect(x, y, width, height)
        self.color = "black"
        self.x = x
        self.y = y

    def draw_circle(self, screen):
        pygame.draw.rect(screen, self.color, self.circle, 2, 15)
        