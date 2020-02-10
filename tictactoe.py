#!/usr/bin/env python3


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
        if winner == 'O':
            return 1
        elif winner == 'X':
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
                new_positions.append([i,j])

    #set next turn
    next_turn = ''
    if turn == 'X':
        next_turn = 'O'
    else:
        next_turn = 'X'

    #recurse
    for i in range(len(children)):
        temp_score = minimax(children[i], next_turn, index)
        scores.append(temp_score)

    #get max score if on max turn, vice versa
    if turn == 'X':
        cur_score = min(scores)
        cur_score_ind = scores.index(cur_score)
    else:
        cur_score = max(scores)
        cur_score_ind = scores.index(cur_score)

    #set position of best move
    index[0] = new_positions[cur_score_ind][0]
    index[1] = new_positions[cur_score_ind][1]

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
    pos = [0,0]
    minimax(board, 'O', pos)
    board[pos[0]][pos[1]] = 'O'
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

    if (game_over(board)[1] != ''):
        print_board(board)
        print("~~~ ", game_over(board)[1], " wins! ~~~")
    elif (game_over(board)[1] == ''):
        print_board(board)
        print("--- It's a Draw! ---")



if __name__ == "__main__":
    main()
