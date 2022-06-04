from collections import deque

def BFS(G,s):
    n = len(G)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    queue = deque([s])

    def BFS_visit(u):
        nonlocal G,n,dist,queue

        for v in range(n):
            if G[u][v] and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    while len(queue) > 0:
        BFS_visit(queue.pop())

    return dist

def breaking( G ):
    n = len(G)
    dist1 = BFS(G,0)
    pd,qd = 0,0
    pi,qi = 0,0
    for i in range(n):
        if dist1[i] > pd:
            pi = i

    start = BFS(G,pi)
    for i in range(n):
        if start[i] > qd:
            qi = i

    end = BFS(G,qi)
    for i in range(n):
        if start[i]+end[i] == qd:

