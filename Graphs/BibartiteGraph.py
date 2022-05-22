# Algorytm sprawdza czy graf jest dwudzielny
from collections import deque

def bipartite_graph(G,src):
    n = len(G)
    colors = [-1 for _ in range(n)]
    colors[src] = 0
    Q = deque([src])

    while len(Q) > 0:
        u = Q.pop()
        for v in G[u]:
            if colors[v] == -1:
                colors[v] = 1-colors[u]
                Q.appendleft(v)
            elif colors[v] == colors[u]:
                return False

    return True


G = [[2, 3, 4, 5], [2, 3, 4], [0, 1, 6], [0, 1], [0, 1, 6], [0, 6], [2, 4]]
print(bipartite_graph(G,0))
