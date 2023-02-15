from minimaxAlphaBeta import *

def playerTurn(board):
    Col = input('Choose a Column between 1 and 7: ')
    if not(Col.isdigit()):
        print("Input must be integer!")
        return playerTurn(board)

    playerMove = int(Col) - 1

    if playerMove < 0 or playerMove > 6:
        print("Column must be between 1 and 7!")
        return playerTurn(board)

    if not(isColumnValid(board, playerMove)):
        print("The Column you select is full!")
        return playerTurn(board)


    board = makeMove(board, playerMove, HUMAN_PLAYER)[0]
    playerFourInRow  = findFours(board)
    return board, playerFourInRow

def playerWins(board):
    printBoard(board)
    print('                    '+"HUMAN WINS !!\n")
    playagain = True if input('DO YOU WANT TO PLAY AGAIN(y/n)?').lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFunction()
    return 0

def aiTurn(board,depth):
    aiMove  = MiniMaxAlphaBeta(board, depth, AI_PLAYER)
    board = makeMove(board, aiMove, AI_PLAYER)[0]
    aiFourInRow  = findFours(board)

    return  board, aiFourInRow

def aiWins(board):
    printBoard(board)
    print('                     '+"AI WINS !!!!\n")
    playagain = True if input('DO YOU WANT TO PLAY AGAIN(y/n)?').lower() == 'y' else False
    #saveBoard(board)
    if playagain:
        mainFunction()
    return 0


def getDepth():
    depth = input('ENTER DIFFICULTY(1-5): ')
    if not(depth.isdigit()):
        print('Input must be integer!')
        return getDepth()

    depth = int(depth,10) 

    if depth < 1 or depth > 5:
        print("Difficulty must be between 1 and 5!")
        return getDepth()

    return depth

def mainFunction():
    board = initializeBoard()
    printBoard(board)
    depth = getDepth()
    whileCondition = 1
    whomStart = True if input('DO YOU WANT TO START(y/n)? ').lower() == 'y' else False
    while(whileCondition):
        if isBoardFilled(board) :
            print("GAME OVER\n")
            break

        if whomStart:

            board, playerFourInRow = playerTurn(board)
            if playerFourInRow:
                whileCondition = playerWins(board)
                if whileCondition ==0:
                    break

            #AI
            board, aiFourInRow = aiTurn(board,depth)
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)
  
          
        else:
            #AI
            board, aiFourInRow = aiTurn(board,depth)
            if aiFourInRow:
                whileCondition = aiWins(board)
                if whileCondition ==0:
                    break
            printBoard(board)

            #Human
            board, playerFourInRow = playerTurn(board)
            if playerFourInRow:
                whileCondition = playerWins(board)

                if whileCondition ==0:
                    break

            printBoard(board)

mainFunction()
