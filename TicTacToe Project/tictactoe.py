import random

#PRINT THE BOARD
def display_board(board):
    print('{} | {} | {}'.format(board[7],board[8],board[9]))
    print('---------')
    print('{} | {} | {}'.format(board[4],board[5],board[6]))
    print('---------')
    print('{} | {} | {}'.format(board[1],board[2],board[3]))

#ASSIGN A MARKER TO EACH PLAYER
def player_input():
    player_marker = input("Please pick a marker 'X' or 'O'").upper()
    while player_marker not in 'XO':
        print('Chosen marker not valid')
        player_marker = input("Please pick a marker 'X' or 'O'").upper()
    return player_marker

#PLACE A NEW MARKER INTO THE BOARD
def place_marker(board,marker,position):
    if board[position] == ' ':
        board[position] = marker
    else:
        print('Cannot place a marker in a previously ocuppied position')

#CHECKS IF A PLAYER HAS WON
def win_check(board,mark):
    if (board[1] == board[2] == board[3] == mark):
        return True
    elif (board[4] == board[5] == board[6] == mark):
        return True
    elif (board[7] == board[8] == board[9] == mark):
        return True
    elif (board[7] == board[4] == board[1] == mark):
        return True
    elif (board[8] == board[5] == board[2] == mark):
        return True
    elif (board[9] == board[6] == board[3] == mark):
        return True
    elif (board[7] == board[5] == board[3] == mark):
        return True
    elif (board[9] == board[5] == board[1] == mark):
        return True
    else:
        return False

#DECIDE WHICH PLAYER STARTS
def choose_first():
    return random.randint(1,2)

#CHECK IF THE SPACE IS AVAILABLE
def space_check(board,position):
    return board[position] == ' '

#CHECK IF THE BOARD IS FULL
def full_board_check(board):
    boardstr = ''
    for marker in board:
        boardstr += marker
    return not ' ' in boardstr

#SELECT POSITION FOR THE NEW MARKER
def player_choice(board):
    position = int(input('Where do u want to put the next marker'))
    while not space_check(board,position):
        print('Position not valid, choose again!')
        position = int(input('Where do u want to put the next marker'))
    return position

#ASK FOR ANOTHER GAME
def replay():
    again = input('Wanna play again? (Yes/No)').lower()
    while (again != 'yes') and (again != 'no'):
        print('Write yes or no')
        again = input('Wanna play again? (Yes/No)').lower()

    return again == 'yes'

print('Welcome to Tic Tac Toe')

while(True):
    #Clean board
    board = [' ']*10

    #Choose marker
    print('Choose player 1 marker')
    player1_marker = player_input()
    print('Choose player 2 marker')
    player2_marker = player_input()
    while player2_marker == player1_marker:
        print('Player cannot have the same marker')
        player2_marker = player_input()

    #Choose turn
    game_on = True
    win = False
    turn = choose_first()
    display_board(board)

    while game_on:

        if turn == 1:
            pos = player_choice(board)
            place_marker(board,player1_marker,pos)
            turn = 2
            win = win_check(board,player1_marker)
        elif turn == 2:
            pos = player_choice(board)
            place_marker(board,player2_marker,pos)
            turn = 1
            win = win_check(board,player2_marker)

        print('\n'*100)
        display_board(board)

        if(win):
            print('PLAYER {} WON!'.format(turn))
            game_on = False
        elif(full_board_check(board)):
            print('Board full! GAME ENDED')
            game_on = False

    if not replay():
        break

quit()
