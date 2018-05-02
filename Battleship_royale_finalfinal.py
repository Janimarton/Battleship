from random import randint
import sys
import getpass


player1board, player2board = [], []

def name_input_func():
    player_1 = input("What is your name Player 1?")

def 
player_2 = input("What is your name Player 2?")

# BoardPlacemnet:
for x in range(1, 6):
    player1board.append(["\033[1;34mO\033[0;0m"] * 5)
    player2board.append(["\033[1;36mO\033[0;0m"] * 5)

# Player 1 board printig


def print_board(player1board):
    for row in player1board:
        print(" ".join(row))

# Player 2 board printing


def print_board(player2board):
    for row in player2board:
        print(" ".join(row))

def input_func(y,player_1):
    x = int(input(str(player_1) + "Give me your "+ y +" position!" ))
    if ((x > 5) or x < 1):
        raise ValueError
    return(x)



# Player 1 ship placement
def ship_placement(ship_row_player1, ship_col_player1)
    while True:
        try:
            (ship_row_player1=int(getpass.getpass(str(player_1) + ", give me your ship's X position!")))
            (ship_col_player1=int(getpass.getpass(str(player_1) + ", give me your ship's Y position!")))
            if ((ship_row_player1 > 5) or ship_row_player1 < 1):
                raise ValueError
            if ((ship_col_player1 > 5) or ship_col_player1 < 1):
                raise ValueError
            else:
                break
        except ValueError:
            print("Enter a number between 1 and 5!")
        return (ship_row_player1, ship_col_player1)
            


# Player 2 ship placement row input
while True:
    try:
        ship_row_player2 = int(getpass.getpass(str(player_2) + ", give me your ship's X position!"))
        if ((ship_row_player2 > 5) or ship_row_player2 < 1):
            raise ValueError
        else:
            break
    except ValueError:
        print("Enter a number between 1 and 5!")
        continue

# Player 2 ship placement col input
while True:
    try:
        ship_col_player2 = int(getpass.getpass(str(player_2) + ", give me your ship's Y position!"))
        if ((ship_col_player2 > 5) or ship_col_player2 < 1):
            raise ValueError
        else:
            break
    except ValueError:
        print("Enter a number between 1 and 5!")
        continue

# Player1 guessing
for turn in range(13):
    print("Turn: " + str(turn + 1)), turn + 1

    guess_row_1 = int(input((player_1) + ", guess the enemy ship X position!"))
    guess_col_1 = int(input((player_1) + ", guess the enemy ship Y position!"))

    # Proper table usage 1.Player
    guess_col_1 = guess_col_1 - 1
    guess_row_1 = guess_row_1 - 1

    if guess_row_1 == (ship_row_player2 - 1) and guess_col_1 == (ship_col_player2 - 1):
        print("Victory Royale! You sank the enemy battleship!")
        break
    else:
        if guess_row_1 not in range(0, 5) or \
                guess_col_1 not in range(0, 5):
            print("Oops, that's not even in the ocean.")
        elif player2board[guess_row_1][guess_col_1] == "\033[1;31mX\033[0;0m":
            print("You guessed that one already. Chose a different coordinate!")
        else:
            # guess_col_1 != ship_col_player2 or guess_row_1 != ship_row_player2
            print("You missed!")
            player2board[guess_row_1][guess_col_1] = "\033[1;31mX\033[0;0m"
            print_board(player2board)
        if (turn == 13):
            print("Game Over!")

    # Player2 guessing
    guess_row_2 = int(input((player_2) + ", guess the enemy ship X position!"))
    guess_col_2 = int(input((player_2) + ", guess the enemy ship Y position!"))

    # Proper table usage 2.Player
    guess_col_2 = guess_col_2 - 1
    guess_row_2 = guess_row_2 - 1

    if guess_row_2 == (ship_row_player1 - 1) and guess_col_2 == (ship_col_player1 - 1):
        print("Victory Royale! You sank the enemy battleship!")
        break
    else:
        if guess_row_2 not in range(0, 5) or \
                guess_col_2 not in range(0, 5):
            print("Oops, that's not even in the ocean.")
        elif player1board[guess_row_2][guess_col_2] == "\033[1;31mX\033[0;0m":
            print("You guessed that one already. Chose a different coordinate!")
        else:
            print("You missed!")
            player1board[guess_row_2][guess_col_2] = "\033[1;31mX\033[0;0m"
            print_board(player1board)
        if (turn == 13):
            print("Game Over!")
