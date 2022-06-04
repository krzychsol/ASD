from queue import PriorityQueue


def dijsktraAdj(G1, src):
    n = len(G1)  # ilosc wierzcholkow
    # init
    d = [float("inf") for _ in range(n)]
    p = [None for _ in range(n)]
    vis = [False for _ in range(n)]
    d[src] = 0
    # create priority queue
    q = PriorityQueue()
    for i in range(n):
        q.put((d[i], i))
    # monotonic improve best paths
    while not q.empty():
        tmp = q.get()
        u = tmp[1]
        vis[u] = True
        for v, w in G1[u]:
            # relax
            if vis[v] == False and d[v] > d[u] + w:
                d[v] = d[u] + w
                p[v] = u

    return d,p


def DFS(G, s, t, ds, dt, minDist):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    cnt = 0

    def DFS_visit(u):
        nonlocal G, visited, n, cnt

        visited[u] = True
        for v, w in G[u]:
            if v and ds[v] + dt[v] == minDist:
                print(u, v)
                cnt += 1
            if v and not visited[v]:
                parent[u] = v
                DFS_visit(v)

        visited[u] = False

    DFS_visit(s)
    return cnt if cnt > 0 else None


def paths(G, s, t):
    ds,ps = dijsktraAdj(G, s)
    dt,pt = dijsktraAdj(G, t)
    print(ds,pt)
    minDist = ds[t]
    return DFS(G, s, t, ds, dt, minDist)


G = [[(1, 2), (2, 4)],
     [(0, 2), (3, 11), (4, 3)],
     [(0, 4), (3, 13)],
     [(1, 11), (2, 13), (5, 17), (6, 1)],
     [(1, 3), (5, 5)],
     [(3, 17), (4, 5), (7, 7)],
     [(3, 1), (7, 3)],
     [(5, 7), (6, 3), ]]
s = 0
t = 7
print(paths(G, s, t))
