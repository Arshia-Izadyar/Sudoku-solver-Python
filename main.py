board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]
"""solving the puzzle
    with backtracking
    """


def solve(board):
    """will solve the puzzle using backtracking

    Args:
        board 

    Returns:
        False if there is no solution and retry 
    """
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            #    board ,number, pose
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0

    return False


def valid(board, number, pose):
    """

    Args:
        board 
        number : 1-9 that can be placed on the board
        pose (x, y): pose[i][j] is the position of the number on the board

    Returns:
        bool if the number can be placed on the board or not : 1 , 0
    """
    # check the rows

    for i in range(len(board[0])):
        if board[pose[0]][i] == number and pose[1] != i:
            return False
    # check the columns
    for j in range(len(board)):
        if board[j][pose[1]] == number and pose[0] != j:
            return False

    # check the box
    box_x = pose[1]//3
    box_y = pose[0]//3
    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if board[i][j] == number and (i, j) != pose:
                return False
    return True


def printBoard(board):
    """seprates the board

    Args:
        board 
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('-'*24)
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]), end=' ')


def find_empty(board):
    """finds the empty spot"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row col
    return None
