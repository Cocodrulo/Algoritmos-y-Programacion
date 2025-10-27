from my_iterator import *

def solve(num_queens):
    """
    Using your brute force iterator compute all the
    solutions to place the given number of queens in
    a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions = []
    for board in My_Iterator(num_queens, num_queens).next():
        # Check unique columns directly
        if len(set(board)) != num_queens:
            continue
        
        # Check diagonals using set trick
        diag1 = set()
        diag2 = set()
        valid = True
        
        for r, c in enumerate(board):
            if (r - c) in diag1 or (r + c) in diag2:
                valid = False
                break
            diag1.add(r - c)
            diag2.add(r + c)
        
        if valid:
            solutions.append(board)
    return solutions
