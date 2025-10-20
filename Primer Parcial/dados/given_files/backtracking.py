from typing import Iterable


class Backtracking:
    def __init__(self, d: int, s: int, T: int) -> None:
        """Inicializa el generador de combinaciones.

        d: número de dados (cada combinación debe usar exactamente d valores)
        s: número de caras por dado (valores de 1 a s)
        T: suma máxima permitida (la suma de la combinación debe ser <= T)
        """
        self.d = d
        self.s = s
        self.T = T

    def next(self) -> Iterable[list[int]]:
        """Generador que produce todas las combinaciones de d dados con caras 1..s

        Cada combinación usa todos los dados y su suma es <= T. El generador
        produce cada combinación como una cadena del formato: "1 1 1" (valores
        separados por un espacio). La implementación debe usar 'yield' y no
        usar 'yield from'.
        """
