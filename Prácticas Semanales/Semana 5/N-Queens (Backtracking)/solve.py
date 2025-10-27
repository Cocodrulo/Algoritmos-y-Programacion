
def solve(num_queens):
    """
    Using backtracking compute all the solutions to place the
    given number of queens in a square board.

    :param num_queens: number of queens to place in the board
    :return: list of lists containing all the solutions

    For example, if num_queens = 4 there are two solutions,
    and it returns:
       solutions_list = [ [1, 3, 0, 2], [2, 0, 3, 1] ]

    """

    solutions_list = []

    # solve it here!
    
    def is_solution_valid(solution, level):
        if len(set(solution[:level])) != len(solution[:level]):
            return False
        
        diag1 = set()
        diag2 = set()
        
        for r, c in enumerate(solution[:level]):
            if (r - c) in diag1 or (r + c) in diag2:
                return False
                break
            diag1.add(r - c)
            diag2.add(r + c)

        return True
        
    solution = [-1]*num_queens
    
    def dfs(level):
        if not is_solution_valid(solution, level):
            return
        elif level == num_queens:
            solutions_list.append(solution[:])
            return
        else:
            for digit in range(num_queens):
                solution[level] = digit
                dfs(level+1)
            solution[level] = -1
            return
    
    dfs(0)

    return solutions_list
