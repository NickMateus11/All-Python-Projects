import pygame,time,random,sys

class new_block():
    
    def __init__(self):
        self.blockx = 0 #for list index
        self.blocky = 1
        self.dimension = 18
        self.block_offset = self.dimension + 2
        self.defaultx = 0
        self.defaulty = 0
        randPiece = random.randint(0,7)
        if randPiece == 1: # I-block
            self.color = (25, 255, 255)
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*3, self.defaulty,                     self.dimension, self.dimension]
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
            self.b3 = [self.defaultx,                       self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
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
            
        self.blocks = [self.b1,self.b2,self.b3,self.b4]
        self.xpos = [self.b1[self.blockx],self.b2[self.blockx],self.b3[self.blockx],self.b4[self.blockx]]
        self.ypos = [self.b1[self.blocky],self.b2[self.blocky],self.b3[self.blocky],self.b4[self.blocky]]
        
def main():
    
    pygame.init()
    winx = 600
    winy = 600
    screen = pygame.display.set_mode([winx,winy])
    pygame.display.set_caption('Tetris v1.1')
    screen.fill(pygame.Color('black'))
    clock = pygame.time.Clock()
    FPS = 60
    timer = 0
    
    #background = pygame.Surface(screen.get_size())
    #bg = bg.convert()
    #bg.fill(pygame.Color('black'))
    #screen.blit(background,[0,0])

    #block_list = [make_piece()]
    fall_offset = 0
    shift_offset = 0
    block_list = [new_block()]
    while True:
        if timer > 0: timer -= 1
        else: timer = 0
        clock.tick(FPS)
        screen.fill(pygame.Color('black'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    shift_offset += (-1) * block_list[0].block_offset
                elif event.key == pygame.K_RIGHT:
                    shift_offset += block_list[0].block_offset
                
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            sleep_time = 0.1
        else: sleep_time = 0.5
                
        fall_offset += block_list[0].block_offset
        if fall_offset>winy//2:
            block_list.append(new_block())
            fall_offset = 0
        for piece in block_list:
            for j in range(4):
                if block_list.index(piece) == len(block_list)-1:                        
                    piece.ypos[j] = piece.blocks[j][piece.blocky] + fall_offset
                    piece.xpos[j] = piece.blocks[j][piece.blockx] + winx//2 - piece.block_offset + shift_offset
                block_rect = (piece.xpos[j],piece.ypos[j],piece.blocks[j][-2],piece.blocks[j][-1])
                pygame.draw.rect(screen, piece.color, block_rect)
        
        pygame.display.update()
        time.sleep(sleep_time)
   
if __name__ == '__main__': main()

