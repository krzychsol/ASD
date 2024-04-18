from queue import PriorityQueue


def dijkstra(G1, s):
    n = len(G1)  # ilosc wierzcholkow
    # init
    d = [float("inf")] * n
    p = [None] * n
    vis = [False] * n
    d[s] = 0
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

    return d


def professor(G, s, t):
    dist_student = dijkstra(G, s)
    dist_professor = dijkstra(G, t)

    minDist = float("inf")
    vertex = s
    n = len(G)
    for i in range(n):
        if dist_student[i] + dist_professor[i] < minDist:
            minDist = dist_student[i] + dist_professor[i]
            vertex = i

    return vertex, minDist


