import pygame,time,random,sys

class new_block():
    
    def __init__(self,winx,winy):
        self.winx = winx
        self.winy = winy
        self.dimension = 22
        self.block_offset = self.dimension + 3
        self.defaultx = self.winx//2 - self.block_offset
        self.defaulty = 0
        self.randPiece = random.randint(1,7)
        if self.randPiece == 1: # I-block
            self.color = (25, 255, 255)
            self.base = 0
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*3, self.defaulty,                     self.dimension, self.dimension]
        elif self.randPiece == 2: # J-block
            self.color = (0, 0, 255)
            self.base = 1
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx,                       self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty + self.block_offset, self.dimension, self.dimension]
        elif self.randPiece == 3: # L-block
            self.color = (255, 125, 25)
            self.base = 2
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty - self.block_offset, self.dimension, self.dimension]
        elif self.randPiece == 4: # O-block
            self.color = (255, 255, 25)
            self.base = 0
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx,                       self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
        elif self.randPiece == 5: # s-block            
            self.color = (0, 255, 0)
            self.base = 1
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty - self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty - self.block_offset, self.dimension, self.dimension]            
        elif self.randPiece == 6: # T-block
            self.color = (255, 25, 255)
            self.base = 1
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty - self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty,                     self.dimension, self.dimension]
        elif self.randPiece == 7:                # z-block
            self.color = (255, 0, 0)
            self.base = 2
            self.b1 = [self.defaultx,                       self.defaulty,                     self.dimension, self.dimension]
            self.b2 = [self.defaultx + self.block_offset,   self.defaulty,                     self.dimension, self.dimension]
            self.b3 = [self.defaultx + self.block_offset,   self.defaulty + self.block_offset, self.dimension, self.dimension]
            self.b4 = [self.defaultx + self.block_offset*2, self.defaulty + self.block_offset, self.dimension, self.dimension]
            
        self.blocks = [self.b1,self.b2,self.b3,self.b4]
        self.rect = []
        for i in range(4):
            self.rect.append(pygame.Rect(self.blocks[i][0],self.blocks[i][1],self.blocks[i][2],self.blocks[i][3]))
            
    def move_x(self,offset):
        for i in range(4):
            self.rect[i].x += offset
            
    def move_y(self,offset):
        for i in range(4):
            self.rect[i].y += offset
            
    def rotate(self,direction):
        if self.randPiece != 4: #dont even rotate the square
            pre_rotate_lowest = self.get_lowest()
            self.base_block = self.rect[self.base]
            for i in range(4):
                if i == self.base:
                    continue
                deltax = (self.rect[i].x - self.base_block.x) * direction #order matters
                deltay = (self.base_block.y - self.rect[i].y) * direction  
                deltax,deltay = deltay,deltax #switch deltas
                self.rect[i].x = self.base_block.x + deltax
                self.rect[i].y = self.base_block.y + deltay
            #if self.randPiece != 1: # dont adjust the I block
            new_deltay = pre_rotate_lowest - self.get_lowest()
            self.move_y(new_deltay)
            
    def get_lowest(self):
        lowest = 0
        for i in range(4):
            if self.rect[i].y > lowest:#lowest is actually highest y val
                lowest = self.rect[i].y
        return lowest
    
    def get_lowest_index(self):         
        lowest = 0
        for i in range(4):
            if self.rect[i].y > lowest:#lowest is actually highest y val
                lowest = self.rect[i].y
                index = i
        return index
    
    def is_collision(self,piece_list):
        for i in range(4):
            for piece in piece_list:
                if self.rect[i].collidelist(piece.rect) != -1:
                    return True               
        
    def draw_block(self,screen):
        for i in range(4):
            try:
                block_rect = (self.rect[i].x,self.rect[i].y,self.rect[i][2],self.rect[i][3])
                if self.rect[i].y >= 50 :
                    pygame.draw.rect(screen, self.color, block_rect)
            except: continue

def validate_move(piece_list,move_type,move_val): #reverts move if invalid
    if piece_list[-1].is_collision(piece_list[:-1]):
        move_type(-move_val)
    #if move_type != piece_list[-1].rotate: #not a rotation
    for i in range(4): #check wall collisions
        if piece_list[-1].rect[i].x < 100 or piece_list[-1].rect[i].x >= 600-100:
            move_type(-move_val)

def drop_layers(piece_list,row_y):    
    for piece in piece_list:
        for j in range(len(row_y)):
            for i in range(len(piece.rect)):
                if piece.rect[i].y < row_y[j]:
                    piece.rect[i].y += piece.block_offset                    
        
def is_tetris(piece_list):
    rect_checkers = []
    for i in range(piece_list[0].winy//piece_list[0].block_offset):
        rect_checkers.append(pygame.Rect(100,i*piece_list[0].block_offset,piece_list[0].dimension,piece_list[0].dimension))
    for j in range((piece_list[0].winx-200)//piece_list[0].block_offset):
        for i in range(len(rect_checkers)-1,-1,-1):
            for piece in piece_list:
                found = False
                if rect_checkers[i].collidelist(piece.rect) != -1:
                    found = True
                    break
            if found == False:
                del rect_checkers[i]
        for i in range(len(rect_checkers)):
            rect_checkers[i].x += piece_list[0].block_offset
    if len(rect_checkers) > 0:
        y_list = []
        for rect in rect_checkers:
            y_list.append(rect.y)
        row_y = sorted(y_list)
        for piece in piece_list:
            for i in range(len(piece.rect)-1,-1,-1):
                if piece.rect[i].y in row_y:
                    del piece.rect[i]
        return row_y
    else:
        return False
        
def main():
    
    pygame.init()
    winx = 600
    winy = 600
    screen = pygame.display.set_mode([winx,winy])
    pygame.display.set_caption(sys.argv[0].split('\\')[-1])
    screen.fill(pygame.Color('black'))
    clock = pygame.time.Clock()
    FPS = 60
    timer = 0   
    piece_list = [new_block(winx,winy)]
    fall_offset = piece_list[0].block_offset
    shift_offset = piece_list[0].block_offset
    current = -1
    bounds = [[100,43],[100,winy-48],[winx-100,winy-48],[winx-100,43]]
    
    while True:        
        screen.fill(pygame.Color('black'))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #move left
                    piece_list[current].move_x(-shift_offset)
                    validate_move(piece_list,piece_list[current].move_x,-shift_offset)
                elif event.key == pygame.K_RIGHT: #move right
                    piece_list[current].move_x(shift_offset)
                    validate_move(piece_list,piece_list[current].move_x,shift_offset)
                elif event.key == pygame.K_q: #rotate counterclockwise
                    piece_list[current].rotate(-1)
                    validate_move(piece_list,piece_list[current].rotate,-1)
                elif event.key == pygame.K_e: #rotate clockwise
                    piece_list[current].rotate(1)
                    validate_move(piece_list,piece_list[current].rotate,1)
                    
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            wait_time = 0.1
        else: wait_time = 0.5               
            
        for piece in piece_list:
            if piece_list.index(piece) == len(piece_list)-1:
                if timer == 0:
                    piece.move_y(fall_offset)
                if piece.is_collision(piece_list[:current]) or piece_list[current].rect[piece_list[current].get_lowest_index()].y >= winy-50:
                    piece.move_y(-fall_offset)
                    drop_blocks = is_tetris(piece_list)
                    if type(drop_blocks) == list:
                        screen.fill(pygame.Color('black'))
                        pygame.draw.lines(screen, pygame.Color('white'), True, bounds, 4)
                        for each in piece_list:
                            each.draw_block(screen)
                        pygame.display.update()
                        time.sleep(0.5)
                        screen.fill(pygame.Color('black'))
                        drop_layers(piece_list,drop_blocks)                        
                    piece_list.append(new_block(winx,winy))

            piece.draw_block(screen)
            
        pygame.draw.lines(screen, pygame.Color('white'), True, bounds, 4)
        if timer > 0: timer -= 1
        else:
            timer = FPS * wait_time
        clock.tick(FPS)
        pygame.display.update()
   
if __name__ == '__main__': main()

