import pygame


class meteorite():

    def __init__(self,screen):
        self.screen=screen

        self.UN=pygame.image.load("un.png")
        self.rect=self.UN.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.UN,self.rect)
        

