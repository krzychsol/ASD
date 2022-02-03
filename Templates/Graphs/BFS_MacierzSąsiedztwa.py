from collections import deque

def BFS(G,src):
    N = len(G)
    q = deque()
    q.append(src)

    visited = [False]*N
    visited[src] = True
    parent = [-1]*N
    dist = [0]*N

    while q:
        v = q.popleft()
        for u in range(N):
            if G[v][u] == 1 and not visited[u]:
                visited[u] = True
                q.append(u)
                dist[u] = dist[v]+1
                parent[u] = v

    return dist,parent


G = [[0,1,1,1,0,0],
     [1,0,0,0,1,1],
     [1,0,0,0,0,0],
     [1,0,0,0,0,1],
     [0,1,0,0,0,0],
     [0,1,0,1,0,0]]

d,p = BFS(G,0)
print(d,p)