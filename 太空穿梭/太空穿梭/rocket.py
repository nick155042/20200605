import pygame


class Rocket():

    def __init__(self,screen):
        self.screen=screen

        self.HJ=pygame.image.load("hj.png")
        self.rect=self.HJ.get_rect()
        self.screen_rect=screen.get_rect()
        self.moving_right = True
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.HJ,self.rect)
        
