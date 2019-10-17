# functions
def StartGame():
    playing = input('Do you want to play tic tac toe game? (y/n) ')
    if (playing == 'y'):
        print('Start game!')
        Board()
    elif (playing == 'n'):
        print('See you next time ;)')
    else:
        print('Please choose y or n')
        StartGame()

def Board():
    player1_marker = input('Choose you marker (X or O): ')
    if (player1_marker == 'X'):
        player2_marker = 'O'
    elif (player1_marker == 'O'):
        player2_marker = 'X'
    else:
        print('Please choose X or O')
        Board()
    # todo: print board

StartGame()
