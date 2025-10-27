from minigraph import Graph as MiniGraph
from collections import defaultdict
from simple_stack import Stack

def kruskal_mst_dfs(G: MiniGraph):
    """
    Implementa Kruskal detectando ciclos con DFS sobre el MST parcial.

    Pautas:
    - Construye la lista de aristas como (u, v, w) leyendo G.edges(data=True).
    - Ordénalas por (w, u, v) para tener salidas deterministas.
    - Mantén una estructura de adyacencia del MST parcial (no dirigido) para hacer DFS.
    - Antes de añadir (u, v), si ya hay camino u→v en MST parcial, descartas (crearía ciclo).
    - Devuelve siempre un triplete:
      (mst, mst_cost, complete_cost) si el MST se completa 
      o 'None' si el grafo no es conexo.

    Donde:
    - mst es una lista de aristas normalizadas (a, b, w) con a <= b.
    - mst_cost = suma de w en mst.
    - complete_cost = suma de todos los pesos del grafo original.
    """
    
    edges = G.edges(data=True)
    mst = []
    complete_cost = 0
    
    for edge in edges[:]:
        mst.append((edge[2]['weight'], edge[0], edge[1]))
        complete_cost += edge[2]['weight']
    
    ordered = sorted(mst, key=lambda data: data[0])
    completed = False
    
    graph = MiniGraph()
    visited = set()
    
    graph.add_edge(ordered[0][1], ordered[0][2], weight = ordered[0][0])
    
    def dfs(u, final_node):
        nonlocal graph, visited
        
        visited.add(u)
        
        for node in graph.neighbors(u):
            if node not in visited:
                visited.add(u)
                if node == final_node:
                    visited.clear()
                    return False
                if not dfs(node, final_node):
                    return
    
        visited.clear()
        return True
                
    for edge in ordered[1::]:
        if dfs(edge[1], edge[2]):
            graph.add_edge(edge[1], edge[2], weight = edge[0])
        
        if graph.number_of_nodes()-1 == G.number_of_nodes():
            break
        
    mst2 = graph.edges(data=True)
    if len(mst2) > 1:
        mst = []
        mst_cost = 0
    
        for data in mst2:
            mst.append((data[0], data[1], data[2]['weight']))
            mst_cost += data[2]['weight']
        
        return (mst, mst_cost, complete_cost)
        

    # Valor por defecto solo para el esqueleto 
    return None # (mst, mst_cost, complete_cost)
