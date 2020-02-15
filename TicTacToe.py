import sys

#The board locations
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
blankSpot = ' '
theBoard = {1: blankSpot, 2: blankSpot, 3: blankSpot,
            4: blankSpot, 5: blankSpot, 6: blankSpot,
            7: blankSpot, 8: blankSpot, 9: blankSpot}
moves = {1,2,3,4,5,6,7,8,9}
avalibleMoves = {}

#Visual display of the board
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
printBoard(theBoard)

def getAvalibleMoves(board, key):
	theBoard = board
	for i in theBoard.keys():
		if key in theBoard.keys():
			avalibleMoves.append(moves[theBoard[i]]) #theBoard[i] = moves

	print(avalibleMoves)

#Player move information
Player1 = 'X'
Player2 = 'O'

# while True:
getAvalibleMoves(theBoard, key)