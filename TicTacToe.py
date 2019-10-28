# methods
def StartGame():
    playing = input('Do you want to play tic tac toe game? (y/n) ')
    if (playing == 'y'):
        print('Start game!')
        ChooseMarker()
        Game()
    elif (playing == 'n'):
        print('See you next time ;)')
    else:
        print('Please choose y or n')
        StartGame()

def Game():
    starting_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    DisplayBoard(starting_board)
    position=int(input("Please choose position in board"))
    PlaceMarker(starting_board,marker,position)

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
#Start

StartGame()

