from EGZAMIN20.Termin2.zad2testy import runtests
import math


def dist(A, B):
    return math.ceil(math.sqrt(pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2)))


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def KruskalMST(G, V):
    n = len(G)
    res = []
    i = 0
    e = 0
    G = [G[0]] + sorted(G[1::], key=lambda x: abs(G[0][2] - x[2]))
    parent = []
    rank = []

    for v in range(n):
        parent.append(v)
        rank.append(0)

    while e < V - 1:
        u, v, w = G[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            e += 1
            res.append([u, v, w])
            union(parent, rank, x, y)

    minD = float("inf")
    maxD = 0
    for u, v, w in res:
        minD = min(minD, w)
        maxD = max(maxD, w)

    return maxD - minD


def highway(A):
    n = len(A)
    G = []
    m = 0
    for i in range(n):
        for j in range(n):
            flag = False
            if i == j:
                continue
            else:
                G.append([i, j, dist(A[i], A[j])])
                for k in range(len(G)):
                    if G[k] == [j, i, dist(A[j], A[i])]:
                        flag = True
                        break
                if not flag:
                    m += 1

    res = float("inf")
    for e in G:
        G[0], e = e, G[0]
        diff = KruskalMST(G, n)
        res = min(res, diff)

    return res


runtests(highway)
