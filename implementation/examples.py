import networkx as nx

def c6_example() -> nx.DiGraph:
    
    vertices = [('s', {'heuristic': 0, 'open': False}),
                ('a', {'heuristic': 1, 'open': False}),
                ('b', {'heuristic': 1, 'open': False}),
                ('c', {'heuristic': 1, 'open': False}),
                ('d', {'heuristic': 3, 'open': False}),
                ('t', {'heuristic': 0, 'open': False})
               ]

    edges = [('s', 'a', 5), 
             ('a', 'b', 6), 
             ('b', 't', 1), 
             ('s', 'c', 8), 
             ('c', 'd', 4), 
             ('d', 't', 1)
             ]

    G: nx.DiGraph = nx.DiGraph()
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(edges)
    return G

def cities_example() -> nx.DiGraph:

    vertices = [('lfk', {'heuristic': 0, 'open': False}),
                ('tpk', {'heuristic': 24, 'open': False}),
                ('emp', {'heuristic': 63, 'open': False}),
                ('wic', {'heuristic': 143, 'open': False}),
                ('akc', {'heuristic': 163, 'open': False}),
                ('jpn', {'heuristic': 137, 'open': False}),
                ('pbg', {'heuristic': 113, 'open': False}),
                ('bton', {'heuristic': 59, 'open': False}),
                ('kc', {'heuristic': 36, 'open': False}),
                ('bvl', {'heuristic': 160, 'open': False})
               ]

    edges = [('lfk', 'tpk', 26), 
             ('tpk', 'emp', 58), 
             ('lfk', 'bton', 75), 
             ('lfk', 'emp', 81), 
             ('lfk', 'kc', 40), 
             ('kc', 'pbg', 117), 
             ('kc', 'jpn', 182), 
             ('bton', 'jpn', 137), 
             ('emp', 'jpn', 176),
             ('emp', 'akc', 119),
             ('emp', 'wic', 79),
             ('jpn', 'akc', 154),
             ('wic', 'bvl', 183),
             ('jpn', 'bvl', 107),
             ('pbg', 'bvl', 117),
             ('akc', 'bvl', 86)
             ]

    G: nx.Digraph = nx.DiGraph()
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(edges)
    return G
