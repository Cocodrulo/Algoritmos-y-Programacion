import minigraph  as nx
from sys          import maxsize as infinite
from simple_queue import *

def bfs_path_length(graph, first_node):
    """
    Compute the shortest path length of the non-directed graph G
    starting from node first_node. Return a dictionary with the
    distance (in number of steps) from first_node to all the nodes.
    """

    distance = {}                 # Diccionario con la distancia desde 
                                  # firstNode al resto de los nodos.
    for node in graph.nodes():
        distance[node] = infinite

    # solve it here!
    
    stack = Queue()
    visible_nodes = set()
    
    stack.enqueue(first_node)
    visible_nodes.add(first_node)
    distance[first_node] = 0
    
    while not stack.isEmpty():
        current_node = stack.dequeue()
        for node in graph.neighbors(current_node):
            if node not in visible_nodes:
                visible_nodes.add(node)
                stack.enqueue(node)
                distance[node] = distance[current_node]+1

    return distance
