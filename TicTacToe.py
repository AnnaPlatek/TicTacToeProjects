# functions
def StartGame():
    playing = input('Do you want to play tic tac toe game? (y/n) ')
    if (playing == 'y'):
        print('Start game!')
        ChooseMarker()
    elif (playing == 'n'):
        print('See you next time ;)')
    else:
        print('Please choose y or n')
        StartGame()

def ChooseMarker():
    player1_marker = input('Choose you marker (X or O): ')
    if (player1_marker == 'X'):
        player2_marker = 'O'
    elif (player1_marker == 'O'):
        player2_marker = 'X'
    else:
        print('Please choose X or O')
        ChooseMarker()
    # todo: print board


def DisplayBoard(board):
    print("   |   |   ")
    print(" "+board[7]+" | "+board[8]+" | " + board[9])
    print("---|---|---")
    print(" "+board[4]+" | "+board[5]+" | " + board[6])
    print("---|---|---")
    print(" "+board[1]+" | "+board[2]+" | " + board[3])
    print("   |   |   ")

StartGame()
test_board=["#","X","O","X","O","X","O","X","X","X"]
DisplayBoard(test_board)
