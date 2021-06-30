from collections import deque

class Graph:
    def __init__(self,edges,vertices):
        self.adj = [[] for _ in range(vertices)]

        for (src,dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def BFS(G,src):
    q = deque()
    q.append(src)

    visited = [False] * len(G.adj)
    visited[src] = True

    dist = [0]*len(G.adj)
    parent = [0]*len(G.adj)
    parent[src] = -1

    while q:
        v = q.popleft()
        for u in G.adj[v]:
            if not visited[u]:
                visited[u] = True
                dist[u] = dist[v]+1
                parent[u] = v
                q.append(u)

    return dist,parent

if __name__ == '__main__':
    edges = [(0,1), (0,2), (0,3), (1,4), (1,5),(3,5)]

    N = max(max(edges))+1
    G = Graph(edges,N)

    d,p = BFS(G,0)
    print(d,p)