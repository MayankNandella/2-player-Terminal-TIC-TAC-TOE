# ----------- space for all my Global variables---------------

# Game board variable
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# If game is still going
game_still_going = True

# For knowing who won? or if it is a tie?
winner = None

# who's turn is it
current_player = "X"
# ---------------------------------------------|
print("Hello!! , Welcome to TIC TAC TOE")
print("Board for positions")
print("----------")
print("1" + " | " + "2" + " | " + "3")
print("4" + " | " + "5" + " | " + "6")
print("7" + " | " + "8" + " | " + "9")
print("----------")
print("\n")
print("Start your game on this board!")


# functions
# Display board
def display_board():
    print("----------")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("----------")


# playing the game
def play_game():

    # displaying initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # handle a single turn to a current player
        handle_turn(current_player)

        # checking if the game has ended or not
        check_if_game_over()

        # flip to the other player
        flip_player()

    # Declaring the winner
    if winner == "X" or winner == "O" :
        print(winner + " WON!!!")
    if winner == None:
        print("Tie.")


# to handle the turns of the current player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Sorry, spot already taken, Go again")

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # taking global variable
    global winner
    # checking if it is a row win
    row_winner = check_rows()
    # checking if it is a column win
    column_winner = check_columns()
    # checking if it is a diagonals
    diagonal_winner = check_diagonals()
    # get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    # setting up a global variable
    global game_still_going
    # check if any of the rows have all the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        # if we find the winner then game is going to stop
        game_still_going = False
        # to check who is the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    # setting up a global variable
    global game_still_going
    # check if any of the rows have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        # if we find the winner then game is going to stop
        game_still_going = False
        # to check who is the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None


def check_diagonals():
    # setting up a global variable
    global game_still_going
    # check if any of the rows have all the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        # if we find the winner then game is going to stop
        game_still_going = False
        # to check who is the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_if_tie():
    # global variable is being used from above
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False


def flip_player():
    # global variable used from the top
    global current_player
    # if current player is X, then change it to O
    if current_player == "X":
        current_player = "O"
    # if current player is O, then change it to X
    elif current_player == "O":
        current_player = "X"


# ------------Start the execution of the game--------
play_game()
