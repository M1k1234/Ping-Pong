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

plR= Player ('palka.jpg',33,250, 20,70, 10)
plL= Player ('palka.jpg',33,250, 20,70, 10)

ball= GameSprite('ball.png',350,250,25,25,12)

game=True
finish=False
clock = time.Clock()
FPS =90



while game:
    for e in event.get():
        if e.type ==QUIT:
            game=False
               
    if not finish:

        window.fill(background)
        window.blit(plR)
        window.blit(plL)
        window.blit(ball)
        

    
    display.update()
    clock.tick(FPS)