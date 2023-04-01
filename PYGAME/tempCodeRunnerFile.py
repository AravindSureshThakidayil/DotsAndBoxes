 for i in range(2): #DOT INTRO
            screen.fill(BLACK)
            print(text1rect.center)
            print(text2rect.center)
            
            if text1rect.center[0] ==(WIDTH//2):
                p.time.delay(6000)
                break
            text1rect.move_ip(i,0)
            text2rect.move_ip(i,0)
           
            screen.blit(text2,text2rect)
            screen.blit(text1,text1rect)
            screen.blit(text3,(400,100))
          
    