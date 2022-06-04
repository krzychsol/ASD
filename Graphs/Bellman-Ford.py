def numOfVertices(G):
    n = 0
    for i in range(len(G)):
        n = max(n, G[i][0])
        n = max(n, G[i][1])
    n += 1
    return n


def BellmanFord(G, s, t):
    n = numOfVertices(G)
    d = [float("inf")] * n
    d[s] = 0

    for i in range(n - 1):
        for u, v, w in G:
            if d[u] != float("inf") and d[u] + w < d[v]:
                d[v] = d[u] + w

    for u, v, w in G:
        if d[u] != float("inf") and d[u] + w < d[v]:
            return False  # mamy ujemny cykl

    return d[t]


# Graf na liscie krawedzi
G = [[0, 1, -1], [0, 2, 4], [1, 2, 3], [1, 3, 2], [1, 4, 2], [3, 2, 5], [3, 1, 1], [4, 3, -3]]
print(BellmanFord(G, 0, 2))
