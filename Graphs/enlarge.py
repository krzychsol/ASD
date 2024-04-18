from zad2testy import runtests

# Krzysztof Solecki
"""
Opis algorytmu: Algorytm najpierw wykonuje dwa razy BFS (z wirzchołka s oraz t) zwracając tablice odległości do tych wierzchołów.
Potem tworzę tablicę liczników oznaczjącą ile wierzchołków w danej odległości od s znajduje się na najkrótszej ścieżce do t.
Jeżeli dwa wierzchołki pod rząd znajdą się na jedynej najkrótszej ścieżce z s do t to oznacza, że usunięcie krawędzi pomiędzy nimi wydłuży najkrótszą ścieżkę.

Złożoność obliczeniowa: O(V+E), gdzie V to ilość wierzchołków grafu, a E to ilość krawędzi
Złożoność pamięciowa: O(V) 
"""

from collections import deque


def BFS(G, s):
    n = len(G)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    queue = deque([s])

    def BFS_visit(u):
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    while len(queue) > 0:
        BFS_visit(queue.pop())

    return dist


def enlarge(G, s, t):
    n = len(G)
    ds = BFS(G, s)
    dt = BFS(G, t)
    min_lenght = ds[t]
    cnt = [0 for _ in range(min_lenght + 1)]

    for i in range(n):
        if ds[i] + dt[i] == min_lenght:
            cnt[ds[i]] += 1

    wanted = None
    for i in range(min_lenght):
        if cnt[i] == cnt[i + 1] == 1:
            wanted = i
            break

    if wanted is None:
        return None

    for u in range(n):
        if ds[u] == wanted:
            for v in G[u]:
                if ds[v] == ds[u] + 1 and ds[v] + dt[v] == min_lenght:
                    return u, v


runtests( enlarge ) 
