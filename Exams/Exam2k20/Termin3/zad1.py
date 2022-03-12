"O(V+E)"

from EGZAMIN20.Termin3.zad1testy import runtests
from collections import deque

def BFS(G,src):
    n = len(G)
    q = deque()
    q.append(src)

    visited = [False]*n
    visited[src] = True
    height = [0]*n
    height[src] = 0

    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
                height[v] = height[u]+1

    return height

def best_root( L ):
    n = len(L)
    idx = 0
    #1 BFS - szukam najbardziej oddalonego od 0 liscia w drzewie
    h = BFS(L,0)
    maks = max(h)
    for i in range(n):
        if h[i] == maks:
            idx = i
            break
    #2 BFS - puszczam go z tego liscia
    h = BFS(L,idx)
    maks = max(h)
    for i in range(n):
        if h[i] == maks:
            idx = i
            break
    #3 BFS - z najdalej oddalonego wezla od liscia z ktorego puszczalem wyzej
    h2 = BFS(L,idx)
    for i in range(n):
        if h[i] == h2[i]:
            return i

runtests( best_root ) 
