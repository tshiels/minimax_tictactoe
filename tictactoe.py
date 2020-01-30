#!/usr/bin/env python3

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

        i = (x - 1) // 3
        j = (x - 1) % 3
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
    for b in board:
        for i in range(3):
            if (b[i] == ' '):
                b[i] = 'O'
                return
    return

def game_over(board):
    game_over = False
    winner = ''

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

    if (game_over):
        print_board(board)
        print("~~~ ", winner, " wins! ~~~")
    return game_over



def print_board(board):
    print(' ', board[0][0], "|", board[0][1], "|", board[0][2])
    print(" -----------")
    print(' ', board[1][0], "|", board[1][1], "|", board[1][2])
    print(" -----------")
    print(' ', board[2][0], "|", board[2][1], "|", board[2][2])

def create_board():
    b = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]
    return b.copy()

def main():
    turn = 0
    board = create_board()
    while (not game_over(board)):
        if (turn % 2 == 0):
            print_board(board)
            player_turn(board)
        else:
            cpu_turn(board)
        turn += 1



if __name__ == "__main__":
    main()
