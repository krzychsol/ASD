'''from queue import PriorityQueue

def dijsktra(G,L,W,s):
    n = len(G)
    d = [[float("inf"),1]]*n
    #parent = [-1]*n
    q = PriorityQueue()
    for i in range(n):
        if L[i] == W[0]:
            d[i] = [0,1]
            q.put((d[i],i))
    while not q.empty():
        tmp = q.get()
        u = tmp[1]
        if d[u][1] == len(W):
            continue
        print(u)
        for v,w in G[u]:
            print(u, d[u], v, d[v])
            if d[v][0] > d[u][0] + w and L[v] == W[d[u][1]]:
                d[v][0] = d[u][0] + w
                d[v][1] = d[u][1] + 1
                #parent[v] = u
                q.put((d[v],v))
            print(u, d[u], v, d[v])
    print(d)
    return

def letters(G,W):
    L,E = G
    n = len(L)
    G = [[] for _ in range(len(L))]
    for u,v,w in E:
        G[u].append((v,w))
        G[v].append((u,w))
    print(G)
    dijsktra(G,L,W,1)



L = ["k","k","o","o","t","t"]
E = [(0,2,2), (1,2,1), (1,4,3), (1,3,2), (2,4,5), (3,4,1), (3,5,3) ]
G = (L,E)
W = "kto"
letters(G,W)'''

from queue import PriorityQueue


def letters(G, W):
    L, E = G
    n = len(L)

    def relax(u, v, w, idx):
        nonlocal d, parent, Q
        if d[idx][v] > d[idx-1][u] + w:
            d[idx][v] = d[idx-1][u] + w
            parent[idx][v] = u
            Q.put((d[idx][v], idx, v))

    # lista sąsiedztwa
    edges = [[] for _ in range(n)]
    for u, v, w in E:
        edges[u].append([v, w])
        edges[v].append([u, w])

    # inicjalizacja tablic pomocniczych
    parent = [[-1 for _ in range(n)] for __ in range(len(W))]
    d = [[float('inf') for _ in range(n)] for __ in range(len(W))]
    for i in range(n):
        if L[i] == W[0]:
            d[0][i] = 0

    # inicjalizacja kolejki
    Q = PriorityQueue()
    for i in range(n):
        if L[i] == W[0]:
            Q.put((0, 0, i))

    # relaksacja krawędzi po kolei
    while not Q.empty():
        du, idx, u = Q.get()

        for v, w in edges[u]:
            if idx < len(W)-1 and L[v] == W[idx + 1]:
                relax(u, v, w, idx + 1)

    # odtwarzanie wyniku
    m = float('inf')
    pos = len(W) - 1
    for i in range(n):
        if L[i] == W[pos]:
            if d[pos][i] < m:
                m = d[pos][i]
    return m

L = ['k', 'k', 'o', 'o', 't', 't']
E = [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)]
G = (L, E)
W = 'kotok'
print(letters(G,W))
