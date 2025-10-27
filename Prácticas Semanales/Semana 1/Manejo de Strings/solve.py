
def solve(input_list):
    solution = []
    for inp in input_list:
        fullstr = ""
        for char in inp:
            if char.isnumeric():
                fullstr += char
                break;
        
        for char in inp[::-1]:
            if char.isnumeric():
                fullstr += char
                break;
                
        solution.append(int(fullstr))
    
    return sum(solution)
