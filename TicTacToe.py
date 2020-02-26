import sys

#The board locations
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
blankSpot = ' '
theBoard = {1: blankSpot, 2: blankSpot, 3: blankSpot,
            4: blankSpot, 5: blankSpot, 6: blankSpot,
            7: blankSpot, 8: blankSpot, 9: blankSpot}
keyList = list(theBoard.keys())
avalibleMoves = {}

#Visual display of the board
#1:top-L, 2:top-M, 3:top-R
#4:mid-L, 5:mid-M, 6:mid-R
#7:low-L, 8:low-M, 9:low-R
def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[7] + '|' + board[8] + '|' + board[9])
printBoard(theBoard)

#fill avalible spot keys into avalibleMoves and print
def getAvalibleMoves(board):
	theBoard = board
	for i in theBoard.keys():
		if blankSpot in theBoard.values():
			avalibleMoves = keyList.index(i)

	print(avalibleMoves)

#Player move information
Player1 = 'X'
Player2 = 'O'

# while True:
getAvalibleMoves(theBoard)