from EGZAMIN20.Termin2.zad3testy import runtests

def DFS(G):
    n = len(G)
    visited = [False] * n
    stack = []

    def DFSVisit(G, u, visited):
        visited[u] = True
        for v in range(n):
            if not visited[v] and G[u][v] == 1:
                DFSVisit(G,v,visited)
                stack.append(v)

    maks = 0
    idx = 0
    for i in range(n):
        cnt = 0
        for j in range(n):
            if G[i][j] == 1:
                cnt += 1
        if cnt > maks:
            maks = cnt
            idx = i

    for u in range(n):
        if not visited[u] and G[idx][u] == 1:
            DFSVisit(G,u,visited)
            stack.append(u)

    stack.append(idx)
    return stack

def tasks(T):
    n = len(T)
    G = [[0 for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if T[i][j] == 2:
                G[i][j] = 1

    for i in range(n):
        for j in range(i+1,n):
            if T[i][j] == 0 and T[j][i]==0:
                G[i][j] = 1

    return DFS(G)

runtests( tasks )
