class board:
    
    def __init__(self):
        self.outline = outline = """
                             |     |
                          {}  |  {}  |  {}
                        _____|_____|_____
                             |     |
                          {}  |  {}  |  {}
                        _____|_____|_____
                             |     |
                          {}  |  {}  |  {}
                             |     |
                                 """
        self.map = {7:0,8:1,9:2,4:3,5:4,6:5,1:6,2:7,3:8}
        self.moveSet = [7,8,9,4,5,6,1,2,3]
        self.draw()
        self.moveSet = [' ']*9
        
    def draw(self):
        self.grid = self.outline.format(*self.moveSet)
        print(self.grid)
        
    def move_is_legal(self,move):
        return (self.moveSet[self.map[move]] == ' ')
    
    def makeMove(self, move, player):
        self.moveSet[self.map[move]] = player
        
    def isWin(self,player):
        win = False
        for i in range(1,9,3):
            if self.moveSet[self.map[i]]==self.moveSet[self.map[i+1]]==self.moveSet[self.map[i+2]]==player:
                win = True
        for i in range(1,4):
            if self.moveSet[self.map[i]]==self.moveSet[self.map[i+3]]==self.moveSet[self.map[i+6]]==player:
                win = True
        if self.moveSet[self.map[1]]==self.moveSet[self.map[5]]==self.moveSet[self.map[9]]==player or self.moveSet[self.map[3]]==self.moveSet[self.map[5]]==self.moveSet[self.map[7]]==player:
            win = True
        return win
    
    def isTrialWin(self,player,moveSet):
        win = False
        for i in range(1,9,3):
            if moveSet[self.map[i]]==moveSet[self.map[i+1]]==moveSet[self.map[i+2]]==player:
                win = True
        for i in range(1,4):
            if moveSet[self.map[i]]==moveSet[self.map[i+3]]==moveSet[self.map[i+6]]==player:
                win = True
        if moveSet[self.map[1]]==moveSet[self.map[5]]==moveSet[self.map[9]]==player or moveSet[self.map[3]]==moveSet[self.map[5]]==moveSet[self.map[7]]==player:
            win = True
        return win
