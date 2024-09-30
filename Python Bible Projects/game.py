board = [" " for i in range(9)]

def print_board():
    i = 0
    print()
    for j in range(3):
        # print row
        print("| {} | {} | {} |".format(board[i], board[i+1],board[i+2]))
        if (i <= 5):
            print("-"*13)
        i += 3
    print()

def player_move(icon):
    havent_moved = True
    while havent_moved:
        print("{}'s turn!".format(icon))
        choice = int(input("Enter your move (1-9): ").strip())
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            havent_moved = False
        else:
            print("\nThat space is taken!")
            print_board()

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if " " not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X wins!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    print_board()
    if is_victory("O"):
        print("O wins!")
        break
    elif is_draw():
        print("Its a draw!")
        break