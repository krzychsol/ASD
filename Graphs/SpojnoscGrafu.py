from collections import deque

def czySpojny(G):
    n = len(G)
    dist = [-1 for _ in range(n)]
    dist[0] = 0
    Q = deque([0])

    while len(Q) > 0:
        u = Q.pop()
        for v in range(n):
            if G[u][v] and dist[v] == -1:
                dist[v] = dist[u]+1
                Q.appendleft(v)

    for u in range(n):
        if dist[u] == -1:
            return False
    return True


g = [[0, 1, 0, 0, 0, 0, 1],
     [1, 0, 1, 0, 0, 1, 1],
     [0, 1, 0, 1, 1, 0, 0],
     [0, 0, 1, 0, 1, 0, 0],
     [0, 0, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 1],
     [1, 1, 0, 0, 0, 1, 0],
     ]

print(czySpojny(g))