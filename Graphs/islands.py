from zad1testy import runtests

def minDistance(G,dist,visited):
    min = float('inf')
    n = len(G)
    min_idx = 0
    for v in range(n):
        if dist[v][0] < min and visited[v] == False:
            min = dist[v][0]
            min_idx = v

    return min_idx

def islands(G1,A,B):
    n = len(G1)
    dist = [[float('inf'),-1,None] for _ in range(n)]
    dist[A][0] = 0
    dist[A][1] = 0
    dist[A][2] = 0
    visited = [False] * n

    for i in range(n):
        u = minDistance(G1, dist, visited)
        visited[u] = True
        for v in range(n):
            if dist[u][2] == G1[u][v]: continue
            if G1[u][v] > 0 and visited[v] == False \
                    and dist[v][0] > dist[u][0] + G1[u][v]:
                dist[v][0] = dist[u][0] + G1[u][v]
                dist[v][1] = u
                dist[v][2] = G1[u][v]

    if dist[B][1] == -1:
        return None
    return dist[B][0]

runtests( islands ) 
