import random, sys

#The board locations
# theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
#             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
#             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
blankSpot = ' '
theBoard = {1: blankSpot, 2: blankSpot, 3: blankSpot,
            4: blankSpot, 5: blankSpot, 6: blankSpot,
            7: blankSpot, 8: blankSpot, 9: blankSpot}
keyList = list(theBoard.keys())

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
# printBoard(theBoard)

#fill available spot keys into avalibleMoves and print
def getAvailableMoves(board):
	theBoard = board
	avalibleMoves = []

	for i in range(1,len(board)+1):
		if blankSpot == theBoard[i]:
			avalibleMoves.append(i)
	return avalibleMoves

def printAvalibleMoves(avalibleMoves):
	avalibleMoves = getAvailableMoves(avalibleMoves)
	if len(avalibleMoves) == 0:
		print("There are no more avalible moves!")
	print("It is " + currentPlayer + "'s turn, Please pick a space. The available moves are: " + str(avalibleMoves)+ ":")

#Player move information
players = ['X','O']
# player1 = 'X'
# player2 = 'O'
currentPlayer = ''

#Starts the game
print("Welcome to Tic-Tac-Toe! \nPress ENTER to Flip Coin to decide if X or O goes first! Or Press (q) quit.")
start = input()
if start == 'q':
	sys.exit()

#Randomly picks starting player
randomNumber = random.randint(1,2)
if randomNumber == 1:
	currentPlayer = players[0]
else:
	currentPlayer = players[1]

#Runs the game till end or quit
while len(getAvailableMoves(theBoard)) != 0:
	print("Player " + currentPlayer + " goes first!\n")
	printBoard(theBoard)
	getAvailableMoves(theBoard)
	printAvalibleMoves(theBoard)


	move = int(input())
	theBoard[move] = currentPlayer 
	if currentPlayer == players[0]:
		currentPlayer = players[1]
	else:
		currentPlayer = players[0]

	getAvailableMoves(theBoard)
	printBoard(theBoard)

