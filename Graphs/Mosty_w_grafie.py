# algorytm:
# 1) wykonujemy DFS zapisując czasy odwiedzenia
# 2) obliczamy dla każdego wierzchołka funkcję low
#    low[v] = min ( czas odwiedzenia v, low[sąsiedzi ale nie rodzic v], low[dziecko v] )
# 3) mosty to krawędzie (v, parent[v]), gdzie d[v] = low[v]

def bridges(G):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [0 for _ in range(n)]
    low = [float("inf") for _ in range(n)]
    parent = [-1 for _ in range(n)]
    low[0] = 0
    depth = 0

    def DFS_visit(u):
        nonlocal G,n,visited,parent,low,d,depth
        visited[u] = True
        d[u] = low[u] = depth
        depth += 1

        for v in range(n):
            if G[u][v] and not visited[v]:
                parent[v] = u
                DFS_visit(v)
                low[u] = min(low[u],low[v])
            elif G[u][v] and visited[v] and parent[u] != v: #krawędź wsteczna
                low[u] = min(low[u],low[v])

    DFS_visit(0)

    result = []
    for u in range(n):
        if d[u] == low[u] and parent[u] != -1:
            result.append((parent[u],u))
    return result


g = [[0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 1, 0],
     ]

print(bridges(g))