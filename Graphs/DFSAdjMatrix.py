"""class Graph:
    adj = []
    def __init__(self, v, e):

        self.v = v
        self.e = e
        Graph.adj = [[0 for i in range(v)]
                     for j in range(v)]

    def addEdge(self, start, e):
        Graph.adj[start][e] = 1
        Graph.adj[e][start] = 1

    def DFS(self, start, visited):

        print(start, end=' ')
        visited[start] = True

        for i in range(self.v):
            if (Graph.adj[start][i] == 1 and not visited[i]):
                self.DFS(i, visited)

v, e = 5, 4
G = Graph(v, e)
G.addEdge(0, 1)
G.addEdge(0, 2)
G.addEdge(0, 3)
G.addEdge(0, 4)

visited = [False] * v
G.DFS(0, visited)"""


def DFS(G,s,t):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]

    def DFS_visit(u):
        nonlocal G,n,t

        if u == t:
            return

        visited[u]= True
        for v in range(n):
            if G[u][v] and not visited[v]:
                parent[v] = u
                DFS_visit(v)

    DFS_visit(s)
    res = []
    idx = t
    while parent[idx] != -1:
        res.append(idx)
        idx = parent[idx]
    res.reverse()
    return res

G = [[0,0,1,1,0],
     [0,0,0,0,0],
     [1,0,0,0,0],
     [1,0,0,0,1],
     [0,0,0,1,0]]

def intuse(I,x,y):
    n = len(I)
    G = [[0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j: continue
            if I[i][1] == I[j][0] or I[i][0] == I[j][1]:
                G[i][j] = 1

    start = []
    end = []
    for i in range(n):
        if I[i][0] == x:
            start.append(i)
        if I[i][1] == y:
            end.append(i)

    res = []
    for st in start:
        for ends in end:
            res.append(DFS(G,st,ends))

    print(res)

I = [(3,4),(2,5),(1,3),(4,6),(1,4)]
x = 1
y = 6

intuse(I,x,y)
