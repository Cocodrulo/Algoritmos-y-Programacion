from typing import Iterable
from simple_stack import Stack

class BacktrackingIter:
    def __init__(self, d: int, s: int, T: int) -> None:
        self.d = d
        self.s = s
        self.T = T

    def next(self) -> Iterable[list[int]]:
        def is_valid(solution: list[int]) -> bool:
            return sum(solution) <= self.T
        
        stack = Stack()
        stack.push([])

        while not stack.isEmpty():
            solution = stack.pop()

            if not is_valid(solution):
                continue

            if len(solution) < self.d:
                for index in range(self.s, 0, -1):
                    solution.append(index)
                    stack.push(solution[:])
                    solution.pop()
            elif sum(solution) <= self.T:
                yield " ".join(map(str, solution))

class BacktrackingRec:
    def __init__(self, d: int, s: int, T: int) -> None:
        self.d = d
        self.s = s
        self.T = T

    def next(self) -> Iterable[list[int]]:
        def is_valid(solution: list[int]) -> bool:
            return sum(solution) <= self.T
        
        def dfs(solution: list[int]) -> Iterable[list[int]]:
            if not is_valid(solution):
                return

            if len(solution) < self.d:
                for index in range(1, self.s+1):
                    solution.append(index)
                    for sol in dfs(solution):
                        yield sol
                    solution.pop()
            elif sum(solution) <= self.T:
                yield " ".join(map(str, solution))
            
        for solution in dfs([]):
            print(solution)
            yield solution

