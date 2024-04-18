from zad3testy import runtests
from math import inf


class Dist:
    def __init__(self):
        self.normal = inf
        self.jump = inf

    def min(self):
        return min(self.normal, self.jump)


def jumper(G, s, t):
    n = len(G)

    dist = [Dist() for _ in range(n)]
    dist[s].normal = 0
    dist[s].jump = 0

    for u in range(n):
        for v in range(n):
            if not G[u][v]: continue
            for w in range(n):
                if not G[w][u]: continue
                dist[v].jump = min(dist[v].jump, dist[w].normal + max(G[w][u], G[u][v]))
            dist[v].normal = min(dist[v].normal, dist[u].min() + G[u][v])

    return dist[t].min()


runtests(jumper)
