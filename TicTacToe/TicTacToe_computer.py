import random
class computer1:
    
    def __init__(self,game):
        self.game = game
        
    def play(self):
        moveChosen,betterMove = False,False
        availableMoves = self.game.moveSet.count(' ')
        attemptedMoveList = []
        while availableMoves>0:
            self.tempMove = random.randint(1,9)
            if (self.tempMove in attemptedMoveList):
                continue
            attemptedMoveList.append(self.tempMove)
            if not (self.game.move_is_legal(self.tempMove)):
                continue
            availableMoves-=1
            if(self.simulateMove('X')):
                Move = self.tempMove
                betterMove = True
            if(self.simulateMove('O')):
                Move = self.tempMove
                break
            if not betterMove:
                Move = self.tempMove
        return(Move)
            
    def simulateMove(self,player):
        trialMoveSet = [' ']*9
        for i in range(9):
            trialMoveSet[i] = self.game.moveSet[i]
        trialMoveSet[self.game.map[self.tempMove]] = player
        return (self.game.isTrialWin(player,trialMoveSet))
    
class computer2:
    def __init__(self,game):
        self.game = game
    def play(self):
        valid = False
        while not valid:
            Move = random.randint(1,9)
            if self.game.move_is_legal(Move):
                valid = True
        return(Move)
            
            
            
