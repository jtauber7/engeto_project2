def main():
    print("=" * 30)
    print("""Welcome to Tic Tac Toe
GAME RULES:
Each player can place one mark (or stone) per turn on the 3x3 grid
The WINNER is who succeeds in placing three of their marks in a
* horizontal,
* vertical or
* diagonal row
Let's start the game...""")
    board = [str(i + 1) for i in range(0, 9)]
    player = "x"
    print_board(board)
    board = [" " for i in range(0, 9)]
    while not evaulate_board(board,player):
        if " " not in board:
            print("The game ended with drew.")
            exit()
        if player == "x":
            player = "o"
        else:
            player = "x"
        change_board(board,player,move=get_move(player))
        print_board(board)
    print("=" * 40)
    print(f"Congratulations, the player '{player}' WON!")


def change_board(board,player,move):
    while not move or not 0 < move < 10:
        input_check(board, move)
        move = get_move(player)
    board[move-1] = player


def input_check(board, move):
    if not 0 < move < 9:
        input("This position does't exist, press 'Enter' to try again...")
        return move
    elif board[move] != " ":
        input("This position is not free, press 'Enter' to try again...")
        return move


def get_move(player):
    print("=" * 40)
    move = input(f"Player {player} | Please enter your move number: ")
    if not move.isdigit():
        return False
    move = int(move)
    print("=" * 40)
    print("=" * 40)
    return move

def print_board(board):
    print("-" * 6)
    print("{}|{}|{}".format(*board[0:3]))
    print("-" * 6)
    print("{}|{}|{}".format(*board[3:6]))
    print("-" * 6)
    print("{}|{}|{}".format(*board[6:9]))
    print("-" * 6)

def evaulate_board(board,player):
    return (board[0] == board[1] == board[2] != " " or
    board[3] == board[4] == board[5] != " " or
    board[6] == board[7] == board[8] != " " or
    board[0] == board[3] == board[6] != " " or
    board[1] == board[4] == board[7] != " " or
    board[2] == board[5] == board[8] != " " or
    board[0] == board[4] == board[8] != " " or
    board[2] == board[4] == board[6] != " ")

main()
