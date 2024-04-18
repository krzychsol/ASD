from math import sqrt, ceil


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def dist(A, B):
    return ceil(sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2))


def KruskalMST(G, V, stations):
    n = len(G)
    res = []
    i = 0
    e = 0
    G = sorted(G, key=lambda x: x[2])
    parent = []
    rank = []

    for v in range(n):
        parent.append(v)
        rank.append(0)

    s = len(stations)
    for i in range(s - 1):
        x = find(parent, s)
        y = find(parent, s + 1)
        if x != y:
            union(parent, rank, x, y)

    while e < V - 1:
        u, v, w = G[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            res.append([u, v, w])
            union(parent, rank, x, y)

    return res[-1][2]


def arctic_network(G, stations):
    e = len(G)
    new_G = []
    v = 0
    for i in range(e):
        for j in range(i + 1, e):
            v = max(v, G[i][0], G[i][1], G[j][0], G[j][1])
            if G[i] in stations and G[j] in stations:
                new_G.append([i, j, 0])
                new_G.append([j, i, 0])
            else:
                new_G.append([i, j, dist(G[i], G[j])])
                new_G.append([j, i, dist(G[i], G[j])])

    return KruskalMST(new_G, v, stations)


settlements = [(1, 1), (2, 3), (-5, -1), (-3, 1), (-2, -2), (-2, 1), (6, 4), (5, 2), (-3, -3), (-5, 4)]
receivers = [(-2, 1), (5, 2), (-3, 1)]
print(arctic_network(settlements, receivers))
