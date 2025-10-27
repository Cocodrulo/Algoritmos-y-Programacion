# Branch And Bound: Node class

Definir en node.py una clase Node que permita la implementación del algoritmo Branch and Bound visto en clase. Básicamente recibe en el constructor los parámetros:

_value:_ que indica el valor de la mochila en el nodo actual

_room:_ capacidad restante de la mochila

_index:_ nivel dentro del árbol _(starting_index)_

La función **estimate** debe devolver el valor del Bound correspondiente.

Los Ítems de la mochila vienen almacenados en una estructura de Python de tipo **namedtuple** tal y como se define en la línea 3 del código
