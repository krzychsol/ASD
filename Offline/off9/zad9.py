# Krzysztof Solecki
"""
Opis algorytmu: Alogrytm znajduje maksymalny przepływ metodą Edmondsa-Karpa. W tym celu wykonuje najpierw preprocessing grafu wejściowego
do postaci macierzy VxV przepustowości. Następnie każdą parę u,v wierzchołków łączę z superujściem w grafie i obliczam maksymalny przepływ
ze źródła ropy do superujścia maksymalizując w ten sposób najlepszy przeływ w tym grafie dla wszystkich par wierzchołków.

Złożoność obliczeniowa: O(V^2*V^2E) - V^2 razy wykonuje algorytm Edmondsa Karpa
Złożoność pamięciowa: O(V^2)
"""

from zad9testy import runtests
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


def maxflow(G, s):
    n = len(G)
    v = 0
    for i in range(n):
        v = max(v, G[i][0], G[i][1])
    v += 1
    new_G = [[0 for _ in range(v + 1)] for __ in range(v + 1)]

    for i in range(n):
        new_G[G[i][0]][G[i][1]] = G[i][2]

    flow = 0
    for i in range(v):
        for j in range(i + 1, v):
            if i == j or i == s or j == s:
                continue
            new_G[i][v] = new_G[j][v] = float("inf")
            curr_flow = edmonds_karp(new_G, s, v)
            flow = max(flow, curr_flow)
            new_G[i][v] = new_G[j][v] = 0

    return flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
