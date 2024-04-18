"""
Definiujemy relację znajomości jako symetryczną
Znajomość:
    - pierwszego stopnia to bezpośrednia znajomość
    - drugiego stopnia to bycie znajomym zajomego
    - itd

Szukamy największego stopnia znajomości między wszystkimi
parami osób.
"""

from collections import deque
from math import inf

# dla grafow rzadkich
def BFS(G, s):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [-1 for _ in range(n)]
    queue = deque([s])
    dist[s] = 0

    while len(queue) > 0:
        u = queue.pop()
        visited[u] = True
        for v in G[u]:
            if not visited[v] and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    return dist


def isConnected(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    DFS_visit(0)
    for i in range(n):
        if not visited[i]:
            return False
    return True


def meet_level(G):
    n = len(G)
    if not isConnected(G):
        return inf

    max_level = 0
    for v in range(n):
        dist = BFS(G, v)
        max_level = max(max_level, max(dist))
    return max_level


G = [[1, 5],
     [0, 2],
     [1, 3],
     [2, 4],
     [3, 5],
     [0, 4, 6, 7],
     [5],
     [5, 8],
     [7, 9],
     [8]]


# dla gestych
def floyd_warshall(G):
    n = len(G)

    for u in range(n):
        for v in range(n):
            for k in range(n):
                G[u][v] = min(G[u][v], G[u][k] + G[k][v])

    return G


def meet_level_v2(G):
    n = len(G)
    G = floyd_warshall(G)

    max_level = 0
    for el in G:
        print(el)

    for u in range(n):
        for v in range(u + 1, n):
            if G[u][v] == inf:
                return inf
            max_level = max(max_level, G[u][v])

    return max_level


G2 = [[0, 1, inf, inf, inf, 1, inf, inf, inf, inf],
      [1, 0, 1, inf, inf, inf, inf, inf, inf, inf],
      [inf, 1, 0, 1, inf, inf, inf, inf, inf, inf],
      [inf, inf, 1,0, 1, inf, inf, inf, inf, inf],
      [inf, inf, inf, 1, 0, 1, inf, inf, inf, inf],
      [1, inf, inf, inf, 1, 0, 1, 1, inf, inf],
      [inf, inf, inf, inf, inf, 1,0, inf, inf, inf],
      [inf, inf, inf, inf, inf, 1, inf,0, 1, inf],
      [inf, inf, inf, inf, inf, inf, inf, 1, 0, 1],
      [inf, inf, inf, inf, inf, inf, inf, inf, 1, 0]]

print(meet_level_v2(G2))
