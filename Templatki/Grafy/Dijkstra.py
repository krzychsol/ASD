from queue import PriorityQueue

def printSolution(G,dist):
    for v in range(len(G)):
        print(v,dist[v])

def minDistance(G,dist,visited):
    min = float('inf')
    n = len(G)
    for v in range(n):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_idx = v

    return min_idx

def dijkstra(G,src):
    n = len(G)
    dist = [float('inf')]*n
    dist[src] = 0
    visited = [False]*n

    for cout in range(n):
        u = minDistance(G,dist,visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and visited[v] == False \
                and dist[v] > dist[u]+G[u][v]:
                    dist[v] = dist[u] + G[u][v]

    printSolution(G,dist)

def dijsktraAdj(G1,s,t):
    n = len(G1) #ilosc wierzcholkow
    #init
    d = [float("inf")]*n
    p = [None]*n
    vis = [False]*n
    d[s] = 0
    #create priority queue
    q = PriorityQueue()
    for i in range(n):
        q.put((d[i],i))
    #monotonic improve best paths
    while not q.empty():
        tmp = q.get()
        u = tmp[1]
        vis[u] = True
        for v,w in G1[u]:
            #relax
            if vis[v] == False and d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u

    return d[t]

G1 = [[(1,3),(3,10)],[(2,3),(3,9)],[(0,1)],[(1,2),(4,5)],[]]

G = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 11, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]]

print(dijsktraAdj(G1,0,2))
