from collections import deque

class Graph:
    def __init__(self,edges,N):
        self.adj = [[] for _ in range(N)]

        for (src,dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def BFS(graph,src,discovered,dest):
    q = deque()
    discovered[src] = True
    q.append(src)
    path = []

    while q:
        v = q.popleft()
        for u in graph.adj[v]:
            if u == dest:
                path.append(u)
                print(path)
                break

            if not discovered[u]:
                discovered[u] = True
                q.append(u)
                path.append(u)

if __name__ == '__main__':
    edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]

    N = 15
    graph = Graph(edges,N)
    discovered = [False]*N

    for i in range(N):
        if not discovered[i]:
            BFS(graph,1,discovered,5)