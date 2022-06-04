"""
Czy istnieje w grafie skierowanym dobry początek

Silnie spojne skladowe
Sortujemy graf spojnnych skladowych topologicznie i bierzemy ta pierwszą
lub
Puszczamy DFS i jeśli istnieje jakiś najlepszy początek to będzie to wierzchołek
z najwyższym czasem przetworzenia
"""


def DFS_get_visit_times(G):
    n = len(G)
    visited = [False for _ in range(n)]
    d = [-1 for _ in range(n)]
    time = 0

    def DFS_visit(u):
        nonlocal G, n, visited, d, time
        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v]:
                DFS_visit(v)
        d[u] = time
        time += 1

    for u in range(n):
        if not visited[u]:
            DFS_visit(u)
    return d


def good_start(G):
    n = len(G)
    times = DFS_get_visit_times(G)
    vertex = 0
    max_time = 0
    for i in range(n):
        if times[i] > max_time:
            max_time = times[i]
            vertex = i

    visited = [False for _ in range(n)]

    def DFS_visit(u):
        nonlocal G, n, visited
        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                DFS_visit(v)

    DFS_visit(vertex)
    for i in range(n):
        if not visited[i]:
            return None
    return vertex


G = [[0, 0, 0, 0],
     [1, 0, 1, 0],
     [1, 0, 0, 0],
     [1, 0, 1, 0]]

print(good_start(G))
