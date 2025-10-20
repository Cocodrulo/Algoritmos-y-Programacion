from utils import open_test_file, get_line
from types import SimpleNamespace
from backtracking import BacktrackingIter, BacktrackingRec

MODES = SimpleNamespace(Iter="iterativo", Rec="recursivo")
test_file = 'test1.txt'
input_source = open_test_file(test_file)

mode = MODES.Iter

d, s, T = map(int, get_line(input_source).split())
lines = None

if mode == MODES.Iter:
    lines = list(BacktrackingRec(d, s, T).next())
elif mode == MODES.Rec:
    lines = list(BacktrackingIter(d, s, T).next())

if lines:
    print("\n".join(lines))
    print(f"Número total de soluciones: {len(lines)}")