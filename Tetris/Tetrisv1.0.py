import pygame,time,random,sys

class block():
    
    def __init__(self):
        self.blockx = 0 #for list index
        self.blocky = 1
        self.dimension = 18
        self.block_offset = 20
        self.defaultx = 0
        self.defaulty = 0
        randPiece = random.randint(0,7)
        if randPiece == 1: # I-block
            self.color = (25, 255, 255)
            self.b1 = [self.defaultx,                       self.defaulty, self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty, self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset*2, self.defaulty, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*3, self.defaulty, self.dimension, self.dimension]
        elif randPiece == 2: # J-block
            self.color = (0, 0, 255)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx,                       self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty + self.block_offset, self.dimension, self.dimension]
        elif randPiece == 3: # L-block
            self.color = (255, 125, 25)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty - self.block_offset, self.dimension, self.dimension]
        elif randPiece == 4: # O-block
            self.color = (255, 255, 25)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx,                        self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset,                     self.dimension, self.dimension]
        elif randPiece == 5: # s-block            
            self.color = (0, 255, 0)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty - self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty - self.block_offset, self.dimension, self.dimension]
            
        elif randPiece == 6: # T-block
            self.color = (255, 25, 255)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty - self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
        else:                # z-block
            self.color = (255, 0, 0)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty + self.block_offset, self.dimension, self.dimension]
        self.block = [self.b1,self.b2,self.b3,self.b4]

def main():
    
    pygame.init()
    winx = 600
    winy = 600
    screen = pygame.display.set_mode([winx,winy])
    pygame.display.set_caption('Tetris v1.0')
    screen.fill(pygame.Color('black'))
    
    #background = pygame.Surface(screen.get_size())
    #bg = bg.convert()
    #bg.fill(pygame.Color('black'))
    #screen.blit(background,[0,0])

    #block_list = [make_piece()]
    fall_offset = 0
    while True:
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit(); sys.exit()
                
        
        #draw_game(block_list)
        
        piece = block()
        for i in range(4):
            block_rect = (piece.block[i][piece.blockx]+winx//2,piece.block[i][piece.blocky]+fall_offset,piece.block[i][2],piece.block[i][3])
            pygame.draw.rect(screen, piece.color, block_rect)
        
        pygame.display.update()
        time.sleep(0.75)
   
if __name__ == '__main__': main()

