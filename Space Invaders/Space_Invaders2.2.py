import pygame,time,os,random
from pygame.locals import*

def GAME():
    pygame.init()
    surfacex=400#surface y size
    surfacey=400#surface x size
    surface=pygame.display.set_mode([surfacex,surfacey])
    global bulletHits
    bulletHits=0
    global bulletMisses
    bulletMisses=0
    move_direction=0#0 is move right, 1 is move left
    enemy_direction=0#used to find which direction enemy moves
    enemyY=1

    #Declare class obj_player to create player objects
    class obj_player(object):
        def __init__(self):
            self.rect=pygame.Rect(200,350,16,16)#set size of player:(xpos,ypos,xsize,ysize)
        def move(self,dir):
            if dir==0 and self.rect.x<=surfacex-16:#move right
                self.rect.x+=5
            if dir==1 and self.rect.x>=0:#move left
                self.rect.x-=5
    
    #declare class shoot_bullet to create bullet objects
    class shoot_bullet(object):
        def __init__(self):
            list_bullets.append(self)#add all bullets created to a list
            self.rect=pygame.Rect(player.rect.x+8,350,4,8)#set size of bullet
        def update(self):
            global bulletMisses
            if self.rect.y>10:
                self.rect.y-=5#the bullet will move 5 up every tick
            else:#bullet missed
                list_bullets.remove(self)
                bulletMisses+=1
        
            #the loop is used to check if an enemy is colliding with a bullet
            for enemy in list_enemies:
                if self.rect.colliderect(enemy.rect):
                    global bulletHits
                    bulletHits+=1
                    list_bullets.remove(self)
                    list_enemies.remove(enemy)
    class obj_enemy(object):
        def  __init__(self,pos):
            list_enemies.append(self)
            self.rect=pygame.Rect(pos[0],pos[1],16,16)
        def update(self,dir,enemyY):
            self.rect.y+=enemyY*12
            if self.rect.y>277:
                endGame()
            if dir==0:#change dir of movement based on enemy dir variable
                self.rect.x+=2
            if dir==1:
                self.rect.x-=2
        def endGame():
            
    player=obj_player()#initialize a player object since there is only one player a list is not required to store object
    clock=pygame.time.Clock()#declare a variable for the pygame clock to control FPS
    can_shoot=True#used to prevent player from holding down space
    list_bullets=[]#this list will store all bullet objects
    list_enemies=[]#this list will store all enemy objects

    pygame.time.set_timer(USEREVENT+1,2000)#will be used to change direction of enemy movement every 2 seconds

    #loop creates all the enemies and places them on the screen
    for yy in range(5):
        for xx in range(5):
            obj_enemy((35*xx,50+35*yy))
        
    while True:
        
        if len(list_enemies)!=0:
            clock.tick(60)#set FPS
            surface.fill([0,0,0])#fill surface to black
            
            if pygame.event.peek(pygame.QUIT):
                pygame.display.quit()
                quit()
            
            #players controls
            key=pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                move_direction=1
            if key[pygame.K_RIGHT]:
                move_direction=0
            if key[pygame.K_SPACE] and can_shoot==True:#shoot
                can_shoot=False
                shoot_bullet()
            if key[pygame.K_SPACE]==False and can_shoot==False: #reload weapon
                can_shoot=True
            player.move((move_direction))#call make player constantly move in certain direction
            
                #this loop draws and updates positions of all bullets
            for bullet in list_bullets:
                bullet.update()
                pygame.draw.rect(surface,(255,255,255),bullet.rect)
            #this loop draws and updates enemy positions
            for enemy in list_enemies:
                enemy.update(enemy_direction,0)
                pygame.draw.rect(surface,(46,222,16),enemy.rect)
            pygame.draw.rect(surface,(255,255,255),player.rect)
            rect=pygame.Rect(0,278,400,2)
            pygame.draw.rect(surface,pygame.Color("red"),rect)
            
            font = pygame.font.SysFont("monospace", 12)
            color=pygame.Color('white')
            text_hits=font.render("Hits: "+str(bulletHits),True,color)
            surface.blit(text_hits,[5,0])
            text_hits=font.render("Misses: "+str(bulletMisses),True,color)
            surface.blit(text_hits,[70,0])
            
            pygame.display.flip()#redraw surface
    
        for event in pygame.event.get():
            if event.type==USEREVENT+1:#when timer is called change direction of enemy movement
                enemyY+=1
                for enemy in list_enemies:
                    enemy.update(enemy_direction,enemyY)
                if enemy_direction==0:
                    enemy_direction=1
                else:
                    enemy_direction=0
        if len(list_enemies)==0:#win condition and restart function
            key=pygame.key.get_pressed()
            font = pygame.font.SysFont("monospace", 50)
            surface.fill(pygame.Color("black"))
            pygame.display.flip()    
            if key[pygame.K_RETURN]==True:
                GAME()
            colorT=['green','red','yellow','orange','blue']
            randcol=random.randint(0,4)
            colorT1=pygame.Color(colorT[randcol])
            randcol=random.randint(0,4)
            colorT2=pygame.Color(colorT[randcol])
            
            textWin = font.render("YOU WIN", True, colorT1)
            surface.blit(textWin, [75, 150])
            font = pygame.font.SysFont("monospace", 20)
            textRe=font.render("HOLD Enter To Restart",True,colorT2)
            surface.blit(textRe, [65, 200])
            font = pygame.font.SysFont("monospace", 20)
            textAcc=font.render("Accuracy: "+str(round((bulletHits/(bulletHits+bulletMisses))*100,1))+"%",True,color)
            surface.blit(textAcc,[80,80])
            font = pygame.font.SysFont("monospace", 12)
            color=pygame.Color('white')
            text_hits=font.render("Hits: "+str(bulletHits),True,color)
            surface.blit(text_hits,[70,60])
            text_hits=font.render("Misses: "+str(bulletMisses),True,color)
            surface.blit(text_hits,[140,60])
            
            pygame.display.flip()
            time.sleep(0.5)
            if key[pygame.K_RETURN]==True:
                GAME()
            surface.fill(pygame.Color("black"))
            pygame.display.flip()
            time.sleep(0.2)
    #pygame.display.quit()
GAME()