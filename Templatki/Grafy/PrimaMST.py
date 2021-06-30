def printMST(G,parent):
    n = len(G)
    for i in range(1,n):
        print(parent[i], "-",i,"\t",G[i][parent[i]])

def minKey(G,key,visited):
    n = len(G)
    min = float("inf")
    for v in range(n):
        if key[v] < min and visited[v] == False:
            min = key[v]
            min_idx = v
    return min_idx

def primMST(G):
    n = len(G)
    key = [float("inf")]*n
    key[0] = 0
    visited = [False]*n
    parent = [0]*n
    parent[0] = -1

    for i in range(n):
        u = minKey(G,key,visited)
        visited[u] = True

        for v in range(n):
            if G[u][v] > 0 and visited[v] == False and key[v] > G[u][v]:
                key[v] = G[u][v]
                parent[v] = u

    printMST(G,parent)

G = [[0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]]

primMST(G)