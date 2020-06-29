import sys
import pygame
from rocket import Rocket
import game_functions as gf


def run_game():
    #初始化
    pygame.init()
    #設畫面大小為500*400
    screen = pygame.display.set_mode((700, 400))
    #rocket=Rocket(screen)
    #載入圖片
    BG=pygame.image.load("bg.png")
    #設圖片為背景
    screen.blit(BG,(0,0))

    roc = pygame.image.load("hj.png")
    tran = pygame.transform.scale( roc , (75,100) )
    screen.blit(tran,(300,250))

    met = pygame.image.load("un.png")
    tran = pygame.transform.scale( met , (75,100) )
    screen.blit(tran,(300,0))
    
    pygame.display.update
    #標題設為太空穿梭
    pygame.display.set_caption('太空穿梭:)')
    



    
    game_over = False


    while not game_over:
        for event in pygame.event.get():
            # 當使用者結束視窗，程式也結束
            if (event.type ==  pygame. QUIT):
                game_over=True
        pygame.display.flip()
    pygame.quit()
run_game()
