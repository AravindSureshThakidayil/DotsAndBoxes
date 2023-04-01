import pygame as p
import time 
import random 

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    K_KP_ENTER,
    K_RETURN,
    QUIT)


def intro():
        global Entry_win_state
        global running_intro
        for i in range(2): #DOT INTRO
            screen.fill(BLACK)

            screen.blit(First_instrcution,(160,400))
            
            if text1rect.center[0] ==(WIDTH//2):
                while  Entry_win_state==False:
                     for event in p.event.get():
                          if event.type==p.QUIT:
                               p.quit()
                          elif event.type==KEYDOWN:
                               if event.key==K_RETURN:
                                    Entry_win_state=True
                               
                                
                     continue
                else:
                     break
                p.time.delay(6000)
              
                break
            text1rect.move_ip(i,0)
            text2rect.move_ip(i,0)
           
            screen.blit(text2,text2rect)
            screen.blit(text1,text1rect)
            screen.blit(text3,(390,130))
def welcome_screen():#
     screen.blit(text4,(240,100))
     Enter()
     p.display.update()
def Enter():
     screen.blit(play_button,(368,268))
     screen.blit(Second_instruction,(335,350))
     p.display.update()

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
BLUE=(0,0,255) 
PURPLE=(255,255,0)
GREEN=(0,255,255)
WIDTH=800
HEIGHT=600
Entry_key=0
p.init()
screen=p.display.set_mode((WIDTH,HEIGHT))
play_button=p.image.load("assets/play-button.png")


Font=p.font.Font("assets/Montserrat-VariableFont_wght.ttf",64)
Font_welcome=p.font.Font("assets/Montserrat-VariableFont_wght.ttf",100)
font_title=p.font.Font("assets/DeliciousHandrawn-Regular.ttf",100)
font_instru=p.font.Font("assets/DeliciousHandrawn-Regular.ttf",60)
text1=font_title.render("DOTS",True,WHITE,BLACK)
text2=font_title.render("BOXES",True,WHITE,BLACK)
text3=font_instru.render("&",True,WHITE,BLACK)
text4=font_title.render("WELCOME",True,WHITE,BLACK)

First_instrcution=font_instru.render("PRESS ENTER TO START",True,WHITE,BLACK)
Second_instruction=font_instru.render("PRESS",True,WHITE,BLACK)



text1rect=text1.get_rect()
text2rect=text2.get_rect()
text2rect.move_ip(0,200)
text4rect=text4.get_rect()



running_intro=True
Entry_win_state=False
while running_intro:

    for event in p.event.get():
        if event.type==p.QUIT:
            running_intro=False 
        if event.type==KEYDOWN:
            if event.key==K_ESCAPE:
                running_intro =False
            if event.key==K_RETURN:
                 Entry_win_state=True
            if Entry_key==1:
                 import gameplay
            

    intro()
    if Entry_win_state==True:
         screen.fill(BLACK)
         welcome_screen()
       
         Entry_key=1
         if ((abs(p.mouse.get_pos()[0]-368)<=64 and abs(p.mouse.get_pos()[1]-268)<=64)) and (p.mouse.get_pressed()[0]):
                import game
        
         
    

        
    p.display.flip()
    p.display.update()

    
