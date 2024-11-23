#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on board[row][col]

    Args:
        board: The current state of the board
        row: Row to check
        col: Column to check
        N: Size of the board

    Returns:
        Boolean indicating if the position is safe
    """
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False
    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i] == j:
            return False
    return True

def solve_nqueens(N, row=0, board=None, solutions=None):
    """
    Solve N Queens problem

    Args:
        N: Size of the board

    Returns:
        solutions: Solution to the N-queens problem
    """
    if board is None:
        board = [-1] * N
    if solutions is None:
        solutions = []

    if row == N:
        solutions.append([[r, board[r]] for r in range(N)])
        return solutions

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1  # Backtrack

    return solutions

def main():
    """Main function to handle input and error cases"""
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
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
