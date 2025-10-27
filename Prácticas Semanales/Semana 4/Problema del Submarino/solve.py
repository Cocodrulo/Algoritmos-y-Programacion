import minigraph as nx

def solve(input_list):
    all_paths = []
    
    graph = nx.Graph()
    
    for edges_raw in input_list:
        edges = edges_raw.replace("\r", "").split("-")
        graph.add_edge(edges[0], edges[1])

    def dfs(u, current_sol, visibleNodes):
        current_sol.append(u)
        if not u.isupper():
            visibleNodes.add(u)
            
        if u == 'end':
            all_paths.append(current_sol)
        
        for node in graph.neighbors(u):
            if not node in visibleNodes:
                dfs(node, current_sol.copy(), visibleNodes.copy())
              
        return
    
    dfs('start', [], set())

    return len(all_paths), all_paths
