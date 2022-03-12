class Graph:
    def __init__(self, edges,N):
        self.V = N
        self.time = 0
        self.adj = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

    def DFSVisit(self,u,visited,parent,low,disc):
        visited[u] = True
        disc[u] = self.time
        low[u] = self.time
        self.time+=1

        for v in self.adj[u]:
            if not visited[v]:
                parent[v] = u
                self.DFSVisit(v,visited,parent,low,disc)
                low[u] = min(low[u],low[v])
                if low[v] > disc[u]:
                    print(u,v)

            elif v != parent[u]:
                low[u] = min(low[u],disc[v])

    def DFS(self):
        visisted = [False]*self.V
        disc = [float('inf')]*self.V
        low = [float('inf')]*self.V
        parent = [-1]*self.V

        for i in range(self.V):
            if not visisted[i]:
                self.DFSVisit(i,visisted,parent,low,disc)


if __name__ == '__main__':
    edges = [(1,0),(0,2),(2,1),(0,3),(3,4)]
    N = max(max(edges))+1
    G = Graph(edges,N)
    G.DFS()