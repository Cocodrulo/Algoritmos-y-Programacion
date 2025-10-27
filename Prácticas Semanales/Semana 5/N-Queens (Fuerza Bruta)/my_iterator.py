# Copia aqui tu solución del primer ejercicio de esta semana

def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number 
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()

    # Añade tu código aqui
    # ...

    for k in range(len(digits)-1,-1,-1):
        next_digits[k] = (next_digits[k] + 1) % base
        
        if next_digits[k] != 0:
           break
    return next_digits

    
# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 1. Añade código aqui
        self.num_counters = num_digits
        self.base = base

    def is_last_value(self, digits):
        for digit in digits:
            if digit != self.base-1:
                return False
        return True

    def next(self):
        # 2. Añade código aqui
        digits = [0] * self.num_counters
        yield digits

        while not self.is_last_value(digits):
            digits = next_number(digits, self.base)
            yield digits

        # Cuando no quedan valores simplemente retornamos
        return
