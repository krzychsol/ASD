# Dany jest acykliczny, spójny, nieskierowany, ważony graf T (czyli T jest tak naprawdę ważonym
# drzewem). Proszę wskazać algorytm, który znajduje taki wierzchołek t, z którego odległość do
# najdalszego wierzchołka jest minimalna.
from math import inf


def DFS(G, u, distance, parent, visited):
    visited[u] = True
    for v, w in G[u]:
        if not visited[v]:
            if distance[u] + w > distance[v]:
                distance[v] = distance[u] + w

            else:
                distance[v] = distance[u]
            parent[v] = u
            DFS(G, v, distance, parent, visited)


def minimum_distance(G, src):
    n = len(G)
    distance = [0 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    visited = [False for _ in range(n)]
    DFS(G,src,distance,parent,visited)
    max_vert = distance.index(max(distance))

    for i in range(n):
        distance[i] = 0
        visited[i] = False
        parent[i] = -1

    DFS(G,max_vert,distance,parent,visited)
    dist = max(distance)
    start = distance.index(dist)
    diameter = []
    v_idx = start

    while v_idx != -1:
        diameter.append((distance[v_idx],abs(distance[v_idx]-dist),v_idx))
        v_idx = parent[v_idx]

    min_dist = float("inf")
    res_vert = 0
    for v in range(len(diameter)):
        diff = abs(diameter[v][0]-diameter[v][1])
        if diff < min_dist:
            min_dist = diff
            res_vert = diameter[v][2]

    return res_vert


graph = [[(1, 12)],
         [(0, 12), (2, 10), (3, 15), (4, -5)],
         [(1, 10)],
         [(1, 15)],
         [(1, -5), (5, 2), (6, 4)],
         [(4, 2)],
         [(4, 4), (7, -6)],
         [(6, -6), (8, 1), (9, 20), (10, 4)],
         [(7, 1)],
         [(7, 20)],
         [(7, 4)]]
print(minimum_distance(graph, 0))
