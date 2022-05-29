#Krzysztof Solecki
"""
Opis działania algorytmu: Tworzę listę krwędzi z ich wagami. Sortuje ją niemalejąco po wagach krawędzi. Wykonuje E razy algorytm Kruskala za każdym razem
usuwając kolejną krawędź grafu i zwracając maksymalną różnicę czasów budowy dróg. Następnie ją minimalizuje (E to liczba krawędzi grafu).

Złożoność czasowa: O(E^2)
Złożoność pamięciowa: O(E)
"""
from zad8testy import runtests
import math


def distance(x, y):
    return math.ceil(math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2))


def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    elif rank[yroot] > rank[xroot]:
        parent[xroot] = yroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])


def KruskalMST(G, e, v, i):
    edgesCnt = 0
    parent = [u for u in range(v)]
    rank = [0 for _ in range(v)]
    minD = float("inf")
    maxD = 0

    while edgesCnt < v - 1:
        if i >= e:
            return None
        a, b, w = G[i]
        x = find(parent, a)
        y = find(parent, b)

        if x != y:
            minD = min(minD,w)
            maxD = max(maxD,w)
            edgesCnt += 1
            union(parent, rank, x, y)
        i += 1

    return maxD-minD


def highway(A):
    n = len(A)
    m = 0
    G = []
    for i in range(n):
        for j in range(i + 1, n):
            m += 1
            G.append([i, j, distance(A[i], A[j])])

    G = sorted(G, key=lambda x: x[2])
    res = float("inf")
    for pos in range(m - n + 2):
        diff = KruskalMST(G, m, n, pos)
        if diff is None:
            return res
        res = min(res, diff)

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)
