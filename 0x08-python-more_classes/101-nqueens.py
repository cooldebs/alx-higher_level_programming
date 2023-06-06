#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
A program that solves the N queens problem.
"""


from sys import argv

if __name__ == "__main__":
    board = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # initialize a solution of the list
    for i in range(n):
        board.append([i, None])

    def already_exists(y):
        """checks that a queen does not already exist in that y value"""
        for x in range(n):
            if y == board[x][1]:
                return True
        return False

    def reject(x, y):
        """Checks whether or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(board[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """clears the answers from the point of failure"""
        for i in range(x, n):
            board[i][1] = None

    def nqueens(x):
        """recursive backtracking function to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                board[x][1] = y
                if (x == n - 1):  # accepts the solution
                    print(board)
                else:
                    nqueens(x + 1)  # moves on to next x value to continue

    # recursively start process at x = 0
    nqueens(0)
