#!/usr/bin/python3
import sys


def print_solutions(solutions):
    """Print all solutions in the required format."""
    for solution in solutions:
        print(solution)


def is_valid(board, row, col):
    """Check if a queen can be placed at (row, col)."""
    for i in range(row):
        if board[i][1] == col or \
           board[i][1] - board[i][0] == col - row or \
           board[i][1] + board[i][0] == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N queens problem."""
    solutions = []
    board = []

    def solve(row):
        """Recursive function to solve N queens problem."""
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board.append([row, col])
                solve(row + 1)
                board.pop()

    solve(0)
    return solutions


def main():
    """Main function to handle input and solve the problem."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
