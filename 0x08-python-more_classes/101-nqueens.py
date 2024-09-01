#!/usr/bin/python3
"""defines nqueens"""

import sys


def init_board(n):
    """Initialize an n*n sized chessboard"""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a deepcopy of chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Retrun the list lists representation of solved chessboard"""
    solution = []
    for i in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def x(board, row, col):
    """
    Spots on chessboard all spots where non-attacking queens can
    no longer be played
    Args:
        board (list): The current working chessboard
        row (int): The row where a queen was last played
        col (int): The column where a queen was last played
    """
    # x all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # x all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # x all spots below
    for r in range(row + 1, len(board))
    # x all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # x all spots diagonally down to right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x all spots diagonally up to left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c]
        c -= 1
    # x all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # x all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board_row, queens, solutions):
    """
    Recursively solve an N-queens puzzle.
    Args:
        board (list): The current working chessboard
        row (int): The current row
        queens (int): The current number of places queens
        solutions (list): A list of solutions
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)

    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.qrgv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
