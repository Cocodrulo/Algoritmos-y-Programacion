import minigraph as nx

def build_graph(edges_list, num_nodes, num_edges):
    # Crea un grafo no-dirigido
    
    graph = nx.Graph()

    # Añade los vértices del grafo; su numeración debe
    # comenzar en 1 (o, sea, 1, 2, 3, ...)
    
    for node in range(1, num_nodes+1):
        graph.add_node(node)

    # Añade los vértices del grafo
    for edges_str in edges_list:
        edges = edges_str.split(" ")
        graph.add_edge(int(edges[0]), int(edges[1])) 
    

    # Retorna el grafo
    return graph
    