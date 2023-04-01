import pygame as p
import random 

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,)


BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255) 
PURPLE=(255,255,0)
GREEN=(0,255,255)




    
class Player(p.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf=p.Surface((75,25))
        self.surf.fill(RED)
        self.rect=self.surf.get_rect()
    def update(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
    
        if (self.rect.left<0):
            self.rect.left=0
        if self.rect.right>800:
            self.rect.right=800
        if self.rect.top<=0:
            self.rect.top=0
        if self.rect.bottom>=600:
            self.rect.bottom=600

class Enemy(p.sprite.Sprite):
    def __init__(self):
        super(Enemy,self).__init__()
        self.surf=p.surface((20,10))
        self.surf.fill(WHITE)
        self.rect=self.surf.get_rect(center=(random.randint(600+20,600+100),random.randint(0,800)))
        self.speed=random.randint(5,20)
    def update(self):
        self.rect.move=self.rect.move_ip(-self.speed,0)
        if self.rect.right<0:
            self.kill()


p.init()
player= Player()

enemies = p.sprite.Group()
all_sprites=p.sprite.Group()
all_sprites.add(player)
screen=p.display.set_mode((800,600))


running = True
while running:

    for event in p.event.get():
        if event.type==p.QUIT:
            running=False
        
        elif event.type==p.KEYDOWN:
            if event.key==K_ESCAPE:
                running=False

    pressed_keys= p.key.get_pressed()
    player.update(pressed_keys)
    screen.fill(BLACK) 
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect) 
    screen.blit(player.surf,player.rect)
    
    p.display.flip()
    p.display.update()