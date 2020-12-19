
#board

board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-" ]

#display board

def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# play game
def play_game():
    #Display initial board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        flip_player


#handle turns
def handle_turn():
    position = input("Choose a position from 1-9: ")
    position = int(position) -1
    board[position] = "X"
    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # check rows
    # check columns
    # check diagonals
    return

def check_if_tie():
    # check rows
    # check columns
    # check diagonals
    return


play_game()


# check win
    #check rows
    #check columns
    #check diagonals
#check tie
#flip player form player'x' to player'O'