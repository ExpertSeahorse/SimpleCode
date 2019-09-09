# ESTABLISHING VARIABLES
##########################################
x = "X"
o = "O"
board = ['$', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
turn = -1
run = True
tie = True
global work
work = True


# FUNCTIONS
##########################################
def space_check(board, position):
    return board[position] == ' '


def full_board(board):
    for i in range(1, 10):
        if space_check(board, i):
            return True
    return False


def placer(board, marker, position):
    # INPUT VALIDATION
    while position not in range(1, 10) or not space_check(board, position):
        print("Enter the position again: ")
        position = int(input())
    # PLACES VALUE
    board[position] = marker


def win(board, mark):
    # CHECKS IF WINNING CONFIGURATION IS ON THE BOARD
    a = board[7] == board[8] == board[9] == mark
    b = board[4] == board[5] == board[6] == mark
    c = board[1] == board[2] == board[3] == mark
    d = board[1] == board[4] == board[7] == mark
    e = board[2] == board[5] == board[8] == mark
    f = board[3] == board[6] == board[9] == mark
    g = board[1] == board[5] == board[9] == mark
    h = board[7] == board[5] == board[3] == mark

    if a or b or c or d or e or f or g or h:
        return False
    else:
        return True


# RUNNING GAME
##########################################
while run and tie:
    # CHANGES THE MARKER TO BE PLACED ON BOARD
    turn += 1
    if turn % 2 == 0:
        player = x
    else:
        player = o

    # USES INPUT TO FIND WHICH SPACE TO FILL
    print("Enter next position: ")
    while work:
        try:
            position = int(input())
        except ValueError:
            print('got here')
            work = False
        else:
            print('here too')
            work = True
            continue
        print("Enter the position again: ")

    position = int(input())
    placer(board, player, position)

    # GENERATES THE BOARD
    print('\n'*100)
    print("-------------\n"
          "|   |   |   |\n"
          "| {a} | {b} | {c} |\n"
          "|   |   |   |\n"
          "-------------\n"
          "|   |   |   |\n"
          "| {d} | {e} | {f} |\n"
          "|   |   |   |\n"
          "-------------\n"
          "|   |   |   |\n"
          "| {g} | {h} | {i} |\n"
          "|   |   |   |\n"
          "-------------\n"
          .format(a=board[7], b=board[8], c=board[9],
                  d=board[4], e=board[5], f=board[6],
                  g=board[1], h=board[2], i=board[3]))

    # CHECKS IF GAME OVER
    run = win(board, player)
    tie = full_board(board)
    if not run:
        print("Player "+player+" wins!")
    elif not tie:
        print("It's a draw!")
