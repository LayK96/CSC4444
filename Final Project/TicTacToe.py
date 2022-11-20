
board = [ ' ' for x in range(10)]

#method to insert amove into position in the board
def insertMove(letter, pos):
    board[pos] = letter

#Method to check whether or not a position is available
def posFree(pos):
    return board[pos] == ' '

#Method to print the board into terminal
def printBoard(board):
    print('   |   | ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   | ')
    print('------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   | ')
    print('------------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   | ')

#Method to check if  you have won the game
def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[7] == letter and board[5] == letter and board[3] == letter) 
#Method to take in a players move
def playerMove():
    run = True      #This is to run a loop to make sure a player gives a valid number, in the range we want
    while run:
        move = input('Pick a spot to place X, 1-9: ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if posFree(move):
                    run = False
                    insertMove('X', move)
                else:
                    print('Sorry, that spot is taken, try again')
            else:
                print('Please type a number within the range!')
        except: 
            print('Please type a number, in integer form, not string')

#Method for AI to determine its move using minmax algorith
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0        # if we can't find a move, let it be 0, to show there was an error

    #Check if AI has a winning move, or player has a winning move
    for letter in ['O' , 'X']:
        for i in possibleMoves:
            boardCopy = board[:]    #Important note, the "[:]" is to make sure that we actually copy the board, not point to same reference
            boardCopy[i] = letter
            if isWinner(boardCopy, letter):
                move = i
                return move

    #AI does not have winning move, we want to find the BEST possible move with minmax
    #Check if corners are open
    cornersOpen = []       #Start with Corner moves as they give us best option to branch and good coverage
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0: 
        move = selRandom(cornersOpen)
        return move
    #Check if center is open
    if 5 in possibleMoves:
        move = 5
        return move
    #Check edges
    edgesOpen = []       #Start with Corner moves as they give us best option to branch and good coverage
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen) > 0: 
        move = selRandom(edgesOpen)

    return move    

#Method to
def selRandom(list):
    import random
    ln = len(list)
    r = random.randrange(0,ln)
    return list[r]

#Method to determine if board is full, no more slots, call it a tie
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


#Main method to call of the above functions
def main():
    print('Welcome to AI Tic-Tac-Toe')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:  
            print('Sorry, you lose!')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game, AI broek')
            else:
                   insertMove('O', move)
                   print('AI placed an O in position', move)
                   printBoard(board)

            
        else:  
            print('You win!')
            break

    if isBoardFull(board):
        print('Tie or also known as two losers')

main()