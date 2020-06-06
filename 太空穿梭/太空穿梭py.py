import random
import pygame

clock=pygame.time.Clock()

screen = pygame.display.set_mode((500, 400))
BG=pygame.image.load("bg.png")
screen.blit(BG,(0,0))
pygame.display.update
pygame.display.set_caption('太空穿梭:)') 
HJ= pygame.image.load("hj.png")
UN=pygame.image.load("un.png")
pygame.display.set_icon(HJ)



game_over = False


while not game_over:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if (event.type ==  pygame. QUIT):
            game_over=True
    pygame.display.flip()
pygame.quit()
