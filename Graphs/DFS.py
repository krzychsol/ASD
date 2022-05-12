from collections import deque

#lista sasiedztwa
def DFS(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    time = 0
    def DFS_visit(u):
        nonlocal visited,parent,G,n,time
        time += 1
        print("Czas odwiedzenia wierzcholka ",u,time)
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(v)

        time += 1
        print("Czas przetworzenia wierzcholka ",u,time)

    for u in range(n):
        if not visited[u]:
            DFS_visit(u)

G1 = [[1, 3], [0, 2], [1], [0]]

#macierz sasiedztwa
def DFS2(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    time = 0
    def DFS_visit(u):
        nonlocal visited,parent,G,n,time
        time += 1
        print("Czas odwiedzenia wierzcholka ",u,time)
        visited[u] = True

        for v in range(n):
            if G[u][v] == 1 and not visited[v]:
                parent[v] = u
                DFS_visit(v)

        time += 1
        print("Czas przetworzenia wierzcholka ",u,time)

    for u in range(n):
        if not visited[u]:
            DFS_visit(u)

G2 = [[0,1,0,1],
      [1,0,1,0],
      [0,1,0,0],
      [1,0,0,0]]
print(DFS2(G2))