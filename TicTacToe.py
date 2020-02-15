import sys

#The board locations
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
moves = {1,2,3,4,5,6,7,8,9}
key = ' '
#Visual display of the board
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
printBoard(theBoard)

def avalibleMoves(board, key):
	theBoard = board
	for i in theBoard.keys():
		if key in theBoard.keys():
			theBoard[i] = moves

	print(theBoard)

#Player move information
Player1 = 'X'
Player2 = 'O'

# while True:
avalibleMoves(theBoard, key)