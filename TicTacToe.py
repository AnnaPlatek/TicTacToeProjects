# methods
def StartGame():
    playing = input('Do you want to play tic tac toe game? (y/n) ')
    if (playing == 'y'):
        print('Start game!')
        Game()
    elif (playing == 'n'):
        print('See you next time ;)')
    else:
        print('Please choose y or n')
        StartGame()

def Game():
    player1_marker, player2_marker = ChooseMarker()
    starting_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    DisplayBoard(starting_board)
    position=int(input("Please choose position in board: "))
    PlaceMarker(starting_board,player1_marker,position)
    DisplayBoard(starting_board)

def ChooseMarker():
    player_marker = input('Choose you marker (X or O): ').upper()
    if (player_marker == 'X'):
        return ('X', 'O')
    elif (player_marker == 'O'):
        return ('O', 'X')
    else:
        #print('Please choose X or O')
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

def PlaceMarker(board,marker,position):
    board[position]=marker

def Victory(board, marker):

    return ((board[7] == marker and board[8] == marker and board[9] == marker) or  # across the top
            (board[4] == marker and board[5] == marker and board[6] == marker) or  # across the middle
            (board[1] == marker and board[2] == marker and board[3] == marker) or  # across the bottom
            (board[7] == marker and board[4] == marker and board[1] == marker) or  # down the middle
            (board[8] == marker and board[5] == marker and board[2] == marker) or  # down the middle
            (board[9] == marker and board[6] == marker and board[3] == marker) or  # down the right side
            (board[7] == marker and board[5] == marker and board[3] == marker) or  # diagonal
            (board[9] == marker and board[5] == marker and board[1] == marker)) # diagonal

def Space_check(board,position):
    return board[position] == ' ' #True if space, False if not empty

def Full_board_check(board):
    for i in range(1,10):
        if Space_check(board, i):
            return False
    return True


#Run tic tac toe

# todo: welcome players
print("**********Welcome to Tic Tac Toe Game!**********")
# todo: do you want to play - if not: break; if yes: next steps
# todo: players choose their markers
StartGame()
# todo: game choose first player

# todo: generate game board
# todo: check if board is full or if empty places are in board
# todo: player 1 places the marker
# todo: player 2 places the marker
# todo: check if any player wins
# todo: congratulations
# todo: do you want play again?





