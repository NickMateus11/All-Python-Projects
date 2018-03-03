class matrix():
    def __init__(self, rawInput, name):
        self.rawInput = rawInput
        self.name = name
        self.formatMatrix()
        self.show()
    def formatMatrix(self):
        self.Matrix = self.rawInput[1:-1].split(';')
        for i in range(len(self.Matrix)):
            self.Matrix[i] = self.Matrix[i].split(',')
            for j in range(len(self.Matrix[i])):
                self.Matrix[i][j] = float(self.Matrix[i][j])
    def show(self):
        print(self.name,'= \n',end='')
        for i in self.Matrix:
            print('     ',end='')
            for j in i:
                print(j,end='   ')
            print('\n')
    def swapRow(self,RowChoice1,RowChoice2):
        self.Matrix[RowChoice1-1],self.Matrix[RowChoice2-1] = self.Matrix[RowChoice2-1],self.Matrix[RowChoice1-1]
    def scalarRow(self,RowChoice1,scalar):
        for j in range(len(self.Matrix[RowChoice1-1])):
            self.Matrix[RowChoice1-1][j] = self.Matrix[RowChoice1-1][j] * scalar
    def addRow(self,RowChoice1,RowChoice2):
        for j in range(len(self.Matrix[RowChoice1-1])):
            self.Matrix[RowChoice1-1][j] = self.Matrix[RowChoice1-1][j] + self.Matrix[RowChoice2-1][j]
            
            
def menu():
    GuiMenu ='''
        Menu:
    'Matrix'.show()
    'Matrix'.swap(R1,R2)
    'Matrix'.scalar(R1,4)
    'Matrix'.add(R1,R3)        
    '''
    print(GuiMenu)
def formatInput(command): # [ A, scalar, [R1,R2] ] or [ B, show, '' ]
    commandList = [command[0]]+command[2:-1].split('(')
    commandList[2] = commandList[2].split(',')
    return commandList    
def main(): #think {A:'new matrix'} dictionary and add more       
    rawMatrix = input("A = ")
    A = matrix(rawMatrix,'A')
   # rawMatrix = input("B = ")
    #B = matrix(rawMatrix,'B')
    while True:
        command = input()
        try:
            if command=='stop':
                break
            command = formatInput(command)
            
            if command[0].lower() =='a':
                name = A
            #elif command[0].lower()=='b':
            #    name = B
            else:
                raise
            if command[1]=='show':
                name.show()
            elif command[1]=='swapRow':
                RowChoice1 = int(command[2][0][1:])
                RowChoice2 = int(command[2][1][1:])
                name.swapRow(RowChoice1,RowChoice2)
            elif command[1]=='scalarRow':
                RowChoice1 = int(command[2][0][1:])
                scalar = float(command[2][1])
                scalar
                name.scalarRow(RowChoice1,scalar)
            elif command[1]=='addRow':
                RowChoice1 = int(command[2][0][1:])
                RowChoice2 = int(command[2][1][1:])
                name.addRow(RowChoice1,RowChoice2)
            else:
                raise
        
        except:
            print('Error try again')
             
menu() 
main()

