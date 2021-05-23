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

        if key_pressed[K_w] and self.rect.y>5:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y<430:
            self.rect.y += self.speed

    def update_l(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y<430:
            self.rect.y += self.speed
        
        
    

window = display.set_mode((700,500))
#задай фон сцены
display.set_caption('Ping-Pong')
background = 149, 186, 177

plL= Player ('palka.jpg',667,250, 20,70, 10)
plR= Player ('palka.jpg',33,250, 20,70, 10)

ball= GameSprite('ball.png',330,250,40,40,12)

game=True
finish=False
clock = time.Clock()
FPS =90

speed_y = 2
speed_x = 2


font.init()
font=font.Font(None,36)
LoseR=font.render('Проиграл правый!!!',True,(236, 27, 46))
LoseL=font.render('Проиграл левый!!!',True,(236, 27, 46))



while game:
    for e in event.get():
        if e.type ==QUIT:
            game=False
               
    if not finish:

        window.fill(background)


        ball.rect.y += speed_y
        ball.rect.x += speed_x

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
            
        if sprite.collide_rect(plR, ball) or sprite.collide_rect(plL, ball):
            speed_y *= 1
            speed_x *= -1

        if ball.rect.x >650:
            window.blit(LoseR,(250,250))
            game=True
            finish=True

           
        if ball.rect.x <0:
            window.blit(LoseL,(250,250))
            game=True
            finish=True
           


    

        plR.update_r()
        plL.update_l()

        plL.reset()
        plR.reset()
        ball.reset()
        

    
    display.update()
    clock.tick(FPS)