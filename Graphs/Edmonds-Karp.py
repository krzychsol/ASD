import collections


def BFS(G, s, t, F):
    n = len(G)
    parent = [-1 for _ in range(n)]
    parent[s] = -2
    M = [0 for _ in range(n)]
    M[s] = float("inf")
    queue = collections.deque()
    queue.append(s)

    while queue:
        u = queue.popleft()
        for v in range(n):
            if G[u][v] - F[u][v] > 0 and parent[v] == -1:
                parent[v] = u
                M[v] = min(M[u], G[u][v] - F[u][v])
                if v != t:
                    queue.append(v)
                else:
                    return M[t], parent
    return 0, parent


def edmonds_karp(G, src, sink):
    n = len(G)
    max_flow = 0
    F = [[0 for _ in range(n)] for __ in range(n)]
    while True:
        Max, parent = BFS(G, src, sink, F)
        if Max == 0:
            break
        max_flow += Max
        v = sink
        while v != src:
            u = parent[v]
            F[u][v] = F[u][v] + Max
            F[v][u] = F[v][u] - Max
            v = u
    return max_flow
