#**********************GLOBAL VARIABLES*************************

#board

board = ["-" , "-" , "-",
         "-" , "-" , "-",
         "-" , "-" , "-" ]

# If game is still going
game_still_going = True

#Who won? Tie?
winner = None


#Who's turn is it
current_player= "X"

#display board
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


# play game
def play_game():
    # Display initial board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        check_if_game_over()

        # Flip to other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print("The winner is " +  winner)

    elif winner == None:
        print("Its a Tie go home Dumbasses")

# handle a single turn pf turns
def handle_turn(current_player):
    position = input("Choose a position from 1-9: ")
    position = int(position) -1
    board[position] = current_player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # setup global variables into our function
    global winner

    # check rows
    row_winner = check_rows
    # check columns
    column_winner = check_columns
    # check diagonals
    diagonal_winner = check_diagonals
    if row_winner:
        winner = row_winner()
        # there was a win
    elif column_winner:
        winner = column_winner()
        # there was a win
    elif diagonal_winner:
        winner = diagonal_winner()
        # there was a win
    else:
        winner = None
        # there was no win
    return

def check_rows():
    # setup global variable in function
    global game_still_going
    # check if any of the rows have all the same rows and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any of the rows has a match, flag that row as a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O)
    if row_1:
        return board[0] # need any component of the row is fine
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # setup global variable in function
    global game_still_going
    # check if any of the columns have all the same columns and is not empty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any of the column has a match, flag that column as a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return the winner (X or O)
    if column_1:
        return board[0] # need any component of the column is fine
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # setup global variable in function
    global game_still_going
    # check if any of the diagonal have all the same diagonal and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any of the diagonal has a match, flag that diagonal as a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return the winner (X or O)
    if diagonal_1:
        return board[0] # need any component of the column is fine
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():

    return

def flip_player():
    # global variable to be used in the function
    global current_player
    # if current_player is X change it to O
    if current_player == "X":
        current_player = "O"
    # if current_player is O change it to X
    elif current_player == "O":
        current_player = "X"

    return



# check win
    # check rows
    # check columns
    # check diagonals
# check tie
# flip player form player'x' to player'O'



# -----------------------Start Execution-------------------------- #
play_game()
