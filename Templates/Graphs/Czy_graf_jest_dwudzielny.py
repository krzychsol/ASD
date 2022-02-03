from collections import deque

"Używając BFS sprawdzamy czy jest cykl parzystej dlugosci"

class Graph:
    def __init__(self,edges,vertices):
        self.adj = [[] for _ in range(vertices)]

        for (src,dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def BFS(G,src):
    n = len(G.adj)
    q = deque()
    q.append(src)

    visited = [False] * n
    visited[src] = True
    dist = [0]*n

    while q:
        v = q.popleft()
        for u in G.adj[v]:
            if not visited[u]:
                visited[u] = True
                dist[u] = dist[v]+1
                q.append(u)
            elif dist[u] == dist[v]:
                return False

    return True

if __name__ == '__main__':
    edges = [(0,1), (1,2), (2,3), (3,4), (4,5),(5,6),(6,1)]

    N = max(max(edges))+1
    G = Graph(edges,N)

    print(BFS(G,0))
