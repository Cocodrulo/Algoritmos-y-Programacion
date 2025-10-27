# 1. Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    next_digits = digits.copy()

    for index in range(len(next_digits)-1, -1, -1):
        next_digits[index] += 1
        if next_digits[index] < base:
            break
        next_digits[index] = 0
    
    return next_digits
    
# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        self.current_solution = [0]*num_digits
        self.base = base
        self.max_digits = [(self.base-1)]*num_digits

    def next(self):
        while True:
            yield self.current_solution
            if self.current_solution == self.max_digits:
                break
            self.current_solution = next_number(self.current_solution, self.base)
        return
