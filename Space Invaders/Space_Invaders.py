import pygame,time,os,random
from pygame.locals import*

pygame.init()
surfacex=400#surface y size
surfacey=400#surface x size
surface=pygame.display.set_mode([surfacex,surfacey])

move_direction=0#0 is move right, 1 is move left
enemy_direction=0#used to find which direction enemy moves

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
        self.rect.y-=5#the bullet will move 5 up every tick
        
        #the loop is used to check if an enemy is colliding witha bullet
        for enemy in list_enemies:
            if self.rect.colliderect(enemy.rect):
                list_bullets.remove(self)
                list_enemies.remove(enemy)
class obj_enemy(object):
    def __init__(self,pos):
        list_enemies.append(self)
        self.rect=pygame.Rect(pos[0],pos[1],16,16)
    def update(self,dir):
        if dir==0:#change dir of movement based on enemy dir variable
            self.rect.x+=2
        if dir==1:
            self.rect.x-=2
player=obj_player()#initialize a player object since there is only one player a list is not required to store object
clock=pygame.time.Clock()#declare a variable for the pygame clock to control FPS
can_shoot=True#used to prevent player from holding down space
list_bullets=[]#this list will store all bullet objects
list_enemies=[]#this list will store all enemy objects

pygame.time.set_timer(USEREVENT+1,2000)#will be used to change direction of enemy movement every 2 seconds

#loop creates all the enemies and places them on the screen
for yy in range(5):
    for xx in range(5):
        obj_enemy((0+35*xx,50+35*yy))
        
while True:
    clock.tick(60)#set FPS
    surface.fill([0,0,0])#fill surface to black
    
    if pygame.event.peek(pygame.QUIT):
        pygame.display.quit()
        quit()
        
    #players controls
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]==True:
        break
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
        enemy.update(enemy_direction)
        pygame.draw.rect(surface,(46,222,16),enemy.rect)
    pygame.draw.rect(surface,(255,255,255),player.rect)
    pygame.display.flip()#redraw surface
    
    for event in pygame.event.get():
        if event.type==USEREVENT+1:#when timer is called change direction of enemy movement
            if enemy_direction==0:
                enemy_direction=1
            else:
                enemy_direction=0
    if len(list_enemies)==0:#win condition
        print("YOU WIN")
        break
font = pygame.font.SysFont("monospace", 50)
surface.fill(pygame.Color("black"))
pygame.display.flip()    
while True:
    key=pygame.key.get_pressed()
    if key[pygame.K_UP]==True:
        break
    randcol=random.randint(0,4)
    if randcol==0:
        colorT=pygame.Color("green")
    if randcol==1:
        colorT=pygame.Color("red")
    if randcol==2:
        colorT=pygame.Color("yellow")
    if randcol==3:
        colorT=pygame.Color("orange")
    if randcol==4:
        colorT=pygame.Color("blue")
    text = font.render("YOU WIN", True, colorT)
    surface.blit(text, [75, 150])
    pygame.display.flip()
    time.sleep(0.3)
    surface.fill(pygame.Color("black"))
    pygame.display.flip()
    time.sleep(0.3)
pygame.display.quit()