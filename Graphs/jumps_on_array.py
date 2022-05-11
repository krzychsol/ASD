def  canJump(T,i,j):
    a = T[i]
    b = T[j]
    n1 = [0]*10
    n2 = [0]*10
    while a > 0:
        n1[a%10]+=1
        a = a//10
    while b > 0:
        n2[b%10]+=1
        b = b//10
    for i in range(10):
        if n1[i] > 0 and n2[i] > 0:
            return True
    return False

def minDistance(G,dist,visited):
    min = float('inf')
    n = len(G)
    min_idx = 0
    for v in range(n):
        if dist[v] < min and visited[v] == False:
            min = dist[v]
            min_idx = v

    return min_idx

def dijkstra(G,s,t):
    n = len(G)
    dist = [float('inf')]*n
    dist[s] = 0
    visited = [False]*n

    for _ in range(n):
        u = minDistance(G,dist,visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and visited[v] == False \
                and dist[v] > dist[u]+G[u][v]:
                    dist[v] = dist[u] + G[u][v]

    if dist[t] != float("inf"):
        return dist[t]
    return -1

def minCost(T):
    n = len(T)
    G = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if canJump(T,i,j):
                G[i][j] = abs(T[i]-T[j])
                G[j][i] = abs(T[i]-T[j])
    maks = max(T)
    mini = min(T)
    source = 0
    dest = 0
    for i in range(n):
        if T[i] == maks:
            dest = i
        if T[i] == mini:
            source = i

    res = dijkstra(G,source,dest)
    return res

T = [124, 533, 632, 795]
print(minCost(T))