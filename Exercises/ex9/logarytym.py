"""
Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny.


logrytmizujemy krawedzie i Dijkstra lub Bellman
"""
from math import log

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


def logarytmy(G,s,t):
    n = len(G)
    for i in range(n):
        G[i][2] = -1*log(G[i][2],2)
    return BellmanFord(G,s,t)


G = [[0, 1, 2], [0, 2, 1 / 8], [1, 0, 2], [1, 3, 8], [2, 0, 1 / 8], [2, 3, 1 / 16], [3, 1, 8], [3, 2, 1 / 16]]
print(BellmanFord(G,0,3))
