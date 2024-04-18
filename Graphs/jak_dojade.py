def minDistance(G, dist, visited):
    min = float('inf')
    n = len(G)
    min_idx = 0
    for v in range(n):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_idx = v

    return min_idx


def jak_dojade(G, P, d, a, b):
    n = len(G)
    dist = [float('inf')] * n
    dist[a] = 0
    visited = [False] * n
    parent = [-1] * n
    fuel = [0] * n
    fuel[a] = d

    for _ in range(n):
        u = minDistance(G, dist, visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] != -1 and visited[v] == False and dist[v] > dist[u] + G[u][v]:
                if fuel[u] - G[u][v] >= 0:
                    dist[v] = dist[u] + G[u][v]
                    parent[v] = u
                    if v in P:
                        fuel[v] = d
                    else:
                        fuel[v] = fuel[u] - G[u][v]

    res = []
    while b != -1:
        res.append(b)
        b = parent[b]

    if len(res) > 1:
        res.reverse()
        return res
    else:
        return None


G = [[-1, 6, -1, 5, 2],
     [-1, -1, 1, 2, -1],
     [-1, -1, -1, -1, -1],
     [-1, -1, 4, -1, -1],
     [-1, -1, 8, -1, -1]]

P = [0, 1, 3]

print(jak_dojade(G, P, 5, 0, 2))
