class Graph:
    def __init__(self, edges,N):
        self.adj = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)


def DFS(G):
    N = len(G.adj)
    discovered = [False] * N
    parent = [-1]*N
    time = 0

    def DFSVisit(G, u, discovered):
        nonlocal time
        time += 1
        discovered[u] = True
        for v in G.adj[u]:
            if not discovered[v]:
                parent[v] = u
                DFSVisit(G,v,discovered)
        time += 1

    for u in G.adj[0]:
        if not discovered[u]:
            DFSVisit(G,u,discovered)

    return time

if __name__ == '__main__':

    edges = [(0,1),(0,2),(0,3),(1,4),(1,5)]

    N = max(max(edges))+1
    G = Graph(edges, N)

    print(DFS(G))