import pygame

# 初始化 pyGame 引擎
pygame.init()
# 設定 pyGame 遊戲視窗 * 標題 *
pygame.display.set_caption("Hello pygame!")
# 設定 pyGame 遊戲視窗 * 大小 *
win = pygame.display.set_mode((640, 480))
game_over = False
# 遊戲主迴圈
while not game_over:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            game_over = True
# 將遊戲視窗繪製 (貼) 到螢幕上
    pygame.display.flip()
pygame.quit()
