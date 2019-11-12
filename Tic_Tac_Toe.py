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
        if player == "x":
            player = "o"
        else:
            player = "x"
        change_board(board,player,move=get_move(player))
        print_board(board)
    print("=" * 40)
    print(f"Congratulations, the player '{player}' WON!")


def change_board(board,player,move):
    while board[move-1] != " ":
        input("This position is not free, press 'Enter' to try again...")
        move = get_move(player)
    board[move-1] = player

def get_move(player):
    print("=" * 40)
    move = int(input(f"Player {player} | Please enter your move number: "))
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
    if (all(i == player for i in board[0:3]) or all(i == player for i in board[3:6]) or all(i == player for i in board[6:9]) or
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        return True

main()
