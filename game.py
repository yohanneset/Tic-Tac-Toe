
def new_board():
    return [[None] * 3 for _ in range(3)]


def is_valid_pos(idx):
    return 1 <= idx <= 3


def check_winner(board):
    pos_lines = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for line in pos_lines:
        r, c = line[0]
        ch = board[r][c]
        if ch and all(board[i][j] == ch for i, j in line):
            return 1 if ch == 'X' else 2 
    return None
    


def check_draw(board):
    for r in board:
        for c in r:
            if c is None:
                return False
    return True


def get_move():
    while True:
        try:
            row = int(input("Enter row (1-3): "))
            col = int(input("Enter column (1-3): "))
            if is_valid_pos(row) and is_valid_pos(col):
                return (row, col)
            else:
                print("Invalid position! Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


def make_move(board, row, col, turn):
    if board[row-1][col-1] is not None:
        print(f"Square ({row}, {col}) is already taken! Try again.")
        return False
    board[row - 1][col - 1] = "X" if turn % 2 == 0 else "O"
    return True


def render(board):
    print("     1      2      3")
    print("   -------------------")
    for r in range(3):
        print(f" {r+1} |", end="")
        for c in range(3):
            print(f"  {board[r][c] or ' '}  |", end="")
        print("\n   -------------------")


def main():
    print("-----Welcome to Tic Tac Toe-----")
    while True:
        winner = None
        turn = 0
        board = new_board()
        render(board)

        while True:
            print(f"Player {turn % 2 + 1}, It's your turn! ")

            while True:
                row, col = get_move()
                if make_move(board, row, col, turn):
                    break
            render(board)
            winner = check_winner(board)

            if winner:
                print(f"Congratulations! Player {winner} wins!")
                break

            if check_draw(board):
                print("Its a draw!")
                break

            turn += 1
        ch = input("Do you wanna play again? y/n : ").strip().lower()
        if ch != 'y':
            break


if __name__ == '__main__':
    main()