import sys
import pygame


def check_events(rocket):
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                rocket.rect.centerx +=1
                rocket.moving_right=False
    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                rocket.moving_right=True
        elif event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                rocket.moving_right=False
    while True:
        gf.check_events(rocket)
        rocket.update()
