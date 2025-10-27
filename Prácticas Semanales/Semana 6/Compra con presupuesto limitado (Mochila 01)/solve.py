# solve_vpl.py — ESQUELETO (alumnos)
# Entrada:
#   Línea 1: N B
#     - N: número de productos
#     - B: presupuesto (euros enteros)
#   Líneas 2..N+1: nombre precio cantidad
#     - nombre: cadena sin espacios
#     - precio: euros redondeados al alza a entero
#     - cantidad: entero (unidades compradas)
#
# Objetivo:
#   Elegir un subconjunto de productos comprando su cantidad completa, 
#   maximizando la suma de cantidades sin superar B. 
#   Coste de un producto = ceil(precio) * cantidad.

from typing import List, Tuple
from mask_iter import BitmaskIterator

    

def solve_knapsack(budget: int, items: List[Tuple[str, int, int, int]]) -> Tuple[int, List[str]]:
    """
    Selecciona el mejor subconjunto de productos que no exceda el presupuesto,
    maximizando la suma de cantidades compradas.

    Parametros:
    1) budget: Presupuesto total disponible (entero, en euros).
    2) items: Lista de tuplas (name, price_eur, qty, cost_eur), donde:
        - name: nombre del producto (str)
        - price_eur: precio por unidad en euros (int) [no se usa en el cálculo]
        - qty: cantidad/unidades que se compran si se incluye el producto (int)
        - cost_eur: coste total del producto = price_eur * qty (int)

    Criterios de decisión (en este orden):
    1) Mayor suma de cantidades (qty).
    2) A igualdad de cantidades, menor coste total.
    3) Si persiste el empate, lista de nombres elegidos lexicográficamente menor.

    Devuelve: (best_qty, best_set)
        1) best_qty: cantidad total máxima alcanzada (int)
        2) best_set: lista ordenada de nombres de productos seleccionados (List[str])
    """

    # Pista de desempate: mayor cantidad; a igualdad, menor coste; 
    # si persiste, lista de nombres lexicográficamente menor.
    
    result = []
    best_qty = 0
    best_cost = 0
    
    def backtrack(i, total_cost, total_qty, chosen):
        nonlocal result, best_qty, best_cost
        
        if total_cost > budget:
            return
        
        if total_qty > best_qty or (total_qty == best_qty and total_cost > best_cost):
            chosen.sort()
            best_cost = total_cost
            best_qty = total_qty
            result = chosen
        elif total_qty == best_qty and total_cost == best_cost:
            chosen.sort()
            best_cost = total_cost
            best_qty = total_qty
            result = result if result < chosen else chosen
        
        if i < len(items):
            backtrack(i+1, total_cost+items[i][3], total_qty+items[i][2], chosen+[items[i][0]])
            backtrack(i+1, total_cost, total_qty, chosen)

    backtrack(0, 0, 0, [])
    
    return best_qty, list(result) # best_qty, best_set
