from utils import open_test_file, get_line
from backtracking import Backtracking

test_file = 'test1.txt' # Si es None recogerá los datos de la consola
input_source = open_test_file(test_file)

d, s, T = map(int, get_line(input_source).split())
lines = list(Backtracking(d, s, T).next())

if lines:
    print("\n".join(lines))
    print(f"Número total de soluciones: {len(lines)}")