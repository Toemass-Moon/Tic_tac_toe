import os
import random

def display_board(board):
    #clear_output()  # Remember, this only works in jupyter!
    os.system('cls') #windows only
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def player_input():
    
    run = True
    while run:
        mark = input('Player 1: Choose X or O:  ')
        if mark.lower() == 'x':
            return ('X','O')
        if mark.lower()== 'o':
            return ('O', 'X')
def place_marker(board, marker, position):
    board[position] = marker
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))


def choose_first():
    if random.randint(1,2) == 1:
        return 'Player 1'
    else:
        return 'Player 2'
def space_check(board, position):
    
    return board[position] == ' '
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board, i):
            return False
    
    return True
def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Where would you like to go next? '))
        
    return position
def replay():
    
    return input('Would you like to play again? Y or N:  ').lower().startswith('y')

print('Welcome to Tic Tac Toe!')

while True:
    #Set the game up here
    #Set game board
    game_board = [' ']*10
    
    #get markers for both players
    p1_mark, p2_mark = player_input()
    turn = choose_first()
    
    print(turn+' will go first.')
    
    play_on = input('Would you like to play Tic Tac Toe? Y or N: ').lower()
    if play_on == 'y':
        game_on = True
    else: 
        game_on = False
    
    while game_on:
        #Player 1 Turn
        if turn == 'Player 1':
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, p1_mark, position)
            
            if win_check(game_board, p1_mark):
                display_board(game_board)
                print('Congrats Player 1! You won the game!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie. Board is full')
                    game_on = False
                    break
                else:
                    turn = 'Player 2'
            
            
            
        #Player2's turn.
        else:
            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, p2_mark, position)
            
            if win_check(game_board, p2_mark):
                display_board(game_board)
                print('Congrats Player 2! You won the game!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('Tie. Board is full')
                    game_on = False
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break