import TicTacToe_Board as gameBoard
import TicTacToe_computer as computerClass
import time

def main():
    turn = 0
    winner,players = None,None
    while (players!=1 and players!=2 and players!=0):
        players = int(input("How many players? (1 or 2)\n"))
    game = gameBoard.board()
    goodComputer = computerClass.computer1(game)
    if players==0:
        badComputer = computerClass.computer2(game)
    while (turn < 9):            
        player = 'X' if (turn%2==0) else 'O'
        if (players==2) or (players==1 and player=='X'):
            move = int(input("Where would you like to play?\n"))
            if move==-1:
                break
        elif (players == 1 or players ==0) and player == 'O':
            move = goodComputer.play()
            time.sleep(1)
        elif (players == 0):
            move = badComputer.play()
            time.sleep(1)
        try:
            if game.move_is_legal(move):
                game.makeMove(move,player)
                if game.isWin(player):
                    winner = player
                    game.draw()
                    break
            else:
                raise
        except:
            if players == 2 or (players == 1 and player=='X'):
                print("Not a valid move")
            continue
        turn+=1
        game.draw()        
    if winner:
        print("Player {} won".format(player))
    else:
        print("It was a draw")
        
main()
        
