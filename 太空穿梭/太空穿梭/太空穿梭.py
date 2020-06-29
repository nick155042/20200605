import pygame


pygame.init()

Bg = pygame.image.load("bg.png")
screen = pygame.display.set_mode((700, 400))


class Rocket(object):
    
     def __init__(self,x,y):
        self.x , self.y = x, y
        self.oRoc = pygame.image.load("hj.png")
        self.Roc = pygame.transform.scale( self.oRoc , (75,100) )
        self.rect = self.Roc.get_rect()
        
     def draw(self):
        screen.blit(self.Roc,(self.x,self.y))

class Meteorite(object):
     
     def __init__(self,x,y):
        self.x , self. y =x, y
        self.oMet =pygame.image.load("un.png")
        self.Met =pygame.transform.scale(self.oMet,(100,100))
        self.rect=self.Met.get_rect()
     def draw(self):
        screen.blit(self.Met,(self,x,self,y)

rocket = Rocket(300,250)
meteorite=Meteorite(300,0)

    
def Update():
     screen.blit(Bg,(0,0))
     rocket.draw()
     meteorite.draw()
     meteorite.falling()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        rocket.x -= 10

    if keys[pygame.K_RIGHT]:
        rocket.x += 10

    

    
        

game_over = False


while not game_over:
    for event in pygame.event.get():
        # 當使用者結束視窗，程式也結束
        if (event.type ==  pygame. QUIT):
            game_over=True

        Update()

            
    pygame.display.flip()
pygame.quit()
