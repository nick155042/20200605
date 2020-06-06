import random
import pygame

clock=pygame.time.Clock()

# 設置視窗標題為 太空穿梭:)
pygame.display.set_caption('太空穿梭:)') 
# 建立 window 視窗畫布，大小為 640x480
win = pygame.display.set_mode((640, 480))
BG=pygame.image.load("bg.png")
HJ= pygame.image.load("hj.png")
UN=pygame.image.load("un.png")
pygame.display.set_icon(UN)



game_over = False


while not game_over:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if (event.type ==  pygame. QUIT):
            game_over=True
    pygame.display.flip()
pygame.quit()
