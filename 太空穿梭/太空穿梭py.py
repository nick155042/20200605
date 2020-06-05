import pygame

# 初始化
pygame.init()
# 設置視窗標題為 太空穿梭:)
pygame.display.set_caption('太空穿梭:)') 
# 建立 window 視窗畫布，大小為 640x480
window = pygame.display.set_mode((640, 480))
game_over = False
bg=pygame.image.load("bg.png")
HJ= pygame.image.load("hj.png")
while True:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if (event.type ==  pygame. QUIT):
            game_over=True
    pygame.display.flip()
pygame.quit()

