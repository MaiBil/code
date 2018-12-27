import random

def display_board(board):
	print('\n'*15)

	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
	print('----------------')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
	print('----------------')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')


def player_input():
	mark = ''

	while not (mark == 'X') or (mark == 'O'):
		mark = input("Player 1: Do you want to be 'X' or 'O'? ").upper()

	if mark == 'X':
		return ('X', 'O'):
	else:
		return ('O', 'X')


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
	pass


def full_board_check(board):
	pass


def player_choice(board):
	pass

	