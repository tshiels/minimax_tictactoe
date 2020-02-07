#!/usr/bin/env python3
from random import randint

def copy_board(board):
    return [x[:] for x in board]

def convert2d(num):
    i = (num - 1) // 3
    j = (num - 1) % 3
    return i,j

def minimax(board, turn, index):
    endgame, winner = game_over(board)

    #reached terminal node, return score
    if endgame:
        if winner is 'O':
            return 1
        elif winner is 'X':
            return -1
        else:
            return 0
    #expand nodes
    children = []
    new_positions = []
    cur_score = 0
    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                temp = copy_board(board)
                temp[i][j] = turn
                children.append(temp)
                new_positions.append((i,j))
    #recurse
    next_turn = ''
    if turn is 'X':
        next_turn = 'O'
    else:
        next_turn = 'X'

    for i in range(len(children)):
        scores[i] = minimax(children[i], next_turn, index)

    #get min score if on cpu turn, vice versa
    if turn is 'O':
        cur_score = min(scores)
        cur_score_ind = scores.index(min(scores))
    else:
        cur_score = max(scores)
        cur_score_ind = scores.index(max(scores))

    if len(children) == 1:
        index = new_positions[cur_score_ind]

    return cur_score



def player_turn(board):
    x = ''
    i = 0
    j = 0
    while True:
        test = input("Enter X position (1-9): ")
        try:
            x = int(test)
        except ValueError:
            print("invalid input!")
            continue

        i,j = convert2d(x)

        if (x > 9 or x < 1):
            print("Valid positions are #1-9.")
            continue
        elif (board[i][j] != ' '):
            print("Position already taken.")
            continue
        else:
            board[i][j] = 'X'
            break
    return

def cpu_turn(board):
    '''
    for b in board:
        for i in range(3):
            if (b[i] == ' '):
                b[i] = 'O'
                return
    '''
    i = randint(0,2)
    j = randint(0,2)
    while board[i][j] is not ' ':
        i = randint(0,2)
        j = randint(0,2)
        continue
    board[i][j] = 'O'
    return

def game_over(board):
    game_over = False
    draw = True
    winner = ''

    #check draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                draw = False
    if draw is True:
        game_over = True

    #check horizontals
    for x in board:
        if (x[0] == x[1] == x[2] == 'X'):
            winner = 'X'
            game_over = True
        elif (x[0] == x[1] == x[2] == 'O'):
            winner = 'O'
            game_over = True

    #check verticals
    for x in range(3):
        if (board[0][x] == board[1][x] == board[2][x] == 'X'):
            winner = 'X'
            game_over = True
        elif (board[0][x] == board[1][x] == board[2][x] == 'O'):
            winner = 'O'
            game_over = True

    #check diagonals
    if (board[0][0] == board[1][1] == board[2][2] == 'X'):
        winner = 'X'
        game_over = True
    elif (board[0][0] == board[1][1] == board[2][2] == 'O'):
        winner = 'O'
        game_over = True
    elif (board[2][0] == board[1][1] == board[0][2] == 'O'):
        winner = 'O'
        game_over = True
    elif (board[2][0] == board[1][1] == board[0][2] == 'X'):
        winner = 'X'
        game_over = True


    if (game_over and winner is not ''):
        print_board(board)
        print("~~~ ", winner, " wins! ~~~")
    elif (game_over and winner is ''):
        print_board(board)
        print("--- It's a Draw! ---")
    return game_over, winner



def print_board(board):
    print(' ', board[0][0], "|", board[0][1], "|", board[0][2])
    print(" -----------")
    print(' ', board[1][0], "|", board[1][1], "|", board[1][2])
    print(" -----------")
    print(' ', board[2][0], "|", board[2][1], "|", board[2][2])

def main():
    turn = 0
    board = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

    while not game_over(board)[0]:
        if (turn % 2 == 0):
            print_board(board)
            player_turn(board)
        else:
            cpu_turn(board)
        turn += 1



if __name__ == "__main__":
    main()
