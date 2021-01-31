import random, sys

# Author: Meghan
# Date: May/01/2020
# This is a simple game of tictactoe with ascii representation, that repeats and keeps score.

# The board locations
blankSpot = ' '
theBoard = {1: blankSpot, 2: blankSpot, 3: blankSpot,
            4: blankSpot, 5: blankSpot, 6: blankSpot,
            7: blankSpot, 8: blankSpot, 9: blankSpot}

# Win log
scores = [0, 0]


def scoreToString():
    return ("----------\n|X:" + str(scores[0]) + " O:" + str(scores[1]) + "|\n----------")


# Visual display of the board
# 1:top-L, 2:top-M, 3:top-R
# 4:mid-L, 5:mid-M, 6:mid-R
# 7:low-L, 8:low-M, 9:low-R
def printBoard():
    print("\n" + theBoard[1] + '|' + theBoard[2] + '|' + theBoard[3])
    print('-+-+-')
    print(theBoard[4] + '|' + theBoard[5] + '|' + theBoard[6])
    print('-+-+-')
    print(theBoard[7] + '|' + theBoard[8] + '|' + theBoard[9])


# printBoard(theBoard)

# fill available spot keys into avalibleMoves and print
def getAvailableMoves():
    avalibleMoves = []

    for i in range(1, len(theBoard) + 1):
        if blankSpot == theBoard[i]:
            avalibleMoves.append(i)
    return avalibleMoves


def printAvalibleMoves():
    avalibleMoves = getAvailableMoves()
    if len(avalibleMoves) == 0:
        print("There are no more avalible moves!")
    print("\nIt is " + currentPlayer + "'s turn, Please pick a space. The available moves are: " + str(
        avalibleMoves) + ":")


# Player move information
players = ['X', 'O']
# player1 = 'X'
# player2 = 'O'
currentPlayer = ''


# Starts the game
def startGame():
    global currentPlayer
    global theBoard
    # reset board
    theBoard = {1: blankSpot, 2: blankSpot, 3: blankSpot,
                4: blankSpot, 5: blankSpot, 6: blankSpot,
                7: blankSpot, 8: blankSpot, 9: blankSpot}

    print("Welcome to Tic-Tac-Toe! \nPress ENTER to Flip Coin to decide if X or O goes first! Or Press (q) quit.")
    start = input()
    if start == 'q':
        sys.exit()

    # Randomly picks starting player
    randomNumber = random.randint(1, 2)
    if randomNumber == 1:
        currentPlayer = players[0]
    else:
        currentPlayer = players[1]

    print("Player " + currentPlayer + " goes first!\n")
    runGame()


def enterMove(move):
    global currentPlayer
    # Check if move is available
    available_moves = getAvailableMoves()

    if move not in available_moves:
        print("This space is not free, please pick again!")
        printAvalibleMoves()
        enterMove(int(input()))
        return
    theBoard[move] = currentPlayer
    if currentPlayer == players[0]:
        currentPlayer = players[1]
    else:
        currentPlayer = players[0]


# Runs the game till end or quit
def runGame():
    while len(getAvailableMoves()) != 0:
        # print("It's Player " + currentPlayer + " Move!\n")

        getAvailableMoves()
        printAvalibleMoves()

        # Takes in next move
        move = int(input())
        enterMove(move)

        getAvailableMoves()
        printBoard()

        # Win conditions
        if theBoard[1] != blankSpot and theBoard[1] == theBoard[2] == theBoard[3] or \
                theBoard[4] != blankSpot and theBoard[4] == theBoard[5] == theBoard[6] or \
                theBoard[7] != blankSpot and theBoard[7] == theBoard[8] == theBoard[9] or \
                theBoard[1] != blankSpot and theBoard[1] == theBoard[4] == theBoard[7] or \
                theBoard[2] != blankSpot and theBoard[2] == theBoard[5] == theBoard[8] or \
                theBoard[3] != blankSpot and theBoard[3] == theBoard[6] == theBoard[9] or \
                theBoard[1] != blankSpot and theBoard[1] == theBoard[5] == theBoard[9]:
            if currentPlayer == players[0]:
                scores[0] += 1
            else:
                scores[1] += 1
            print("\nPlayer " + str(theBoard[
                                        move]) + " wins! \nThe score is:\n" + scoreToString() + "\nPlay again? (ENTER to continue / (q) to Quit)")
            restart = input()
            if restart == 'q':
                sys.exit()
            else:
                startGame()


if __name__ == '__main__':
    startGame()
