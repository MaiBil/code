import random

def display_board(board):
    print('\n'*35)

    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('----------------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('----------------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def player_input():

    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1 choose 'X' or 'O': ").upper()
        
    if marker.upper() == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


def choose_first():
    first = random.randint(0,1)
    if first == 0:
        return 'Player 1'
    elif first == 1:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position from 1 to 9: '))

    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


print('Welcome to Tic Tac Toe!')

while True:
    theBoard = [' '] * 10
    player1_mark, player2_mark = player_input()
    turn = choose_first()
    print("It is " + turn + "'s turn")

    play_game = input('Do you want to play? (Y/N): ').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False

    
    while game_on:
    
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_mark, position)

            if win_check(theBoard, player1_mark):
                display_board(theBoard)
                print("Congratulations! Player 1 won")
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print("It's a draw")
                break
            else:
                turn = 'Player 2'

        if turn == 'Player 2':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_mark, position)

            if win_check(theBoard, player2_mark):
                display_board(theBoard)
                print("Congratulations! Player 2 won")
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print("It's a draw")
                break
            else:
                turn = 'Player 1'

    if not replay():
        break
