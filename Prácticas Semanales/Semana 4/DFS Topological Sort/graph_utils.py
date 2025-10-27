import minigraph as nx

def build_digraph_with_weights(edges_list, num_nodes, num_edges):
    """ 
    Build the corresponding directed graph with weights. Nodes
    numbering starts with number 1 (that is, nodes are 1,2,3,...)
    """

    # Paso 1: Crear grafo direcional con num_nodes
    graph = nx.DiGraph()

    # Añade los vértices del grafo; su numeración debe
    # comenzar en 1 (o, sea, 1, 2, 3, ...)
    
    for node in range(1, num_nodes+1):
        graph.add_node(node)

    # Añade los vértices del grafo
    for edges_str in edges_list:
        edges = edges_str.split(" ")
        graph.add_edge(int(edges[0]), int(edges[1]), weight = int(edges[2])) 
    

    # Retorna el grafo
    return graph

