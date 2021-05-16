
from random import randint
from pygame import *



class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x, player_y,size_x, size_y ,  player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y  ))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_W] and self.rect.y>5:
            self.rect.y += self.speed

        if key_pressed[K_S] and self.rect.y<610:
            self.rect.y -= self.speed

    def update_l(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y>5:
            self.rect.y += self.speed

        if key_pressed[K_DOWN] and self.rect.y<610:
            self.rect.y -= self.speed
        
        
    

window = display.set_mode((700,500))
#задай фон сцены
display.set_caption('Ping-Pong')
background = 149, 186, 177


font.init()
font2 = font.SysFont('Arial', 36)

font.init()
font3 = font.SysFont('Arial',50)

font.init()
font=font.SysFont('Arial',70)
lose = font.render('YOU LOOOOOOOOSE!!!!!',True,(255,0,0))


game=True
finish=False
clock = time.Clock()
FPS =90



while game:
               
    if not finish:

        window.fill(background)
        

    
    display.update()
    clock.tick(FPS)