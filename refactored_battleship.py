import getpass
import sys
print("\n")
welcome = "\033[1;32mWelcome to Battleship Royale! This is a two player game, you will play on a 5x5 board\033[0;0m"
print(welcome)
player1 = input("What is your name Player 1?")
player2 = input("What is your name Player 2?")

player1board, player2board = [], []
for x in range(1, 6):
    player1board.append(["\033[1;34mO\033[0;0m"] * 5)
    player2board.append(["\033[1;36mO\033[0;0m"] * 5)


def print_board(board):
    for row in board:
        print(" ".join(row))


def input_func(player, coordinate):
    while True:
        try:
            x = int(getpass.getpass(str(player) + " give me your ships" + coordinate + " position!"))
            if ((x > 5) or x < 1):
                raise ValueError
            else:
                return(x)
                break
        except ValueError:
            print("Enter a number between 1 and 5!")


player1_col = input_func(player1, " X ")
player1_row = input_func(player1, " Y ")
player2_col = input_func(player2, " X ")
player2_row = input_func(player2, " Y ")


def guessing_func(playervariable, coordinate):
    while True:
        try:
            guessedvariable = int(input((playervariable) + ", guess the enemy ship " + coordinate + " position!"))
            guessedvariable = guessedvariable - 0
            if ((guessedvariable > 100) or guessedvariable < 1):
                raise ValueError
            else:
                return(guessedvariable)
                break
        except ValueError:
            print("Enter a number between 1 and 5!")


print("The boards will look like this :")
print_board(player1board)
print("\n")
print_board(player2board)


def tipping(guessed1_col, player2_col, guessed1_row, player2_row, player2board):
    player2_col = player2_col - 0
    player2_row = player2_row - 0
    if guessed1_col == (player2_col - 0) and guessed1_row == (player2_row - 0):
        print("\n")
        print("\033[1;32mVictory Royale! You sank the enemy battleship!\033[0;0m")
        print("\n")
        sys.exit()
    else:
        if guessed1_col not in range(0, 6) or \
                guessed1_row not in range(0, 6):
            print("Oops, that's not even in the ocean.")
        elif player2board[(guessed1_row - 1)][(guessed1_col - 1)] == "\033[1;31mX\033[0;0m":
            print("You guessed that one already. Chose a different coordinate!")
        else:
            # guess_col_1 != ship_col_player2 or guess_row_1 != ship_row_player2
            print("You missed!")
            player2board[(guessed1_row - 1)][(guessed1_col - 1)] = "\033[1;31mX\033[0;0m"
            print_board(player2board)
        if (turn == 13):
            print("Game Over!")


def turn():
    for turn in range(13):
        guessed1_col = guessing_func(player1, " X ")
        guessed1_row = guessing_func(player1, " Y ")
        tipping(guessed1_col, player2_col, guessed1_row, player2_row, player2board)
        print("Turn: " + str(turn + 1)), turn + 1
        guessed2_col = guessing_func(player2, " X ")
        guessed2_row = guessing_func(player2, " Y ")
        tipping(guessed2_col, player1_col, guessed2_row, player1_row, player1board)


turn()
