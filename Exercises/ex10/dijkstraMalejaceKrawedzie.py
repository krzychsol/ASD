"""
Dany jest grafG=(V, E), gdzie każda krawędź ma wagę ze zbioru{1,...,|E|} (wagi krawędzi są parami różne). 
Proszę zaproponować algorytm, który dla danych wierzchołków x i y oblicza ścieżkę o najmniejszej sumie wag, 
która prowadzi z x do y po krawędziach o malejących wagach (jeśli ścieżki nie ma to zwracamy inf).

Sortowanie po krawedziach malejaco i dijkstra
"""


class Graph:
    def __init__(self, size):
        self.size = size
        self.arr = [[] for _ in range(size)]
        self.edges = []

    def add_edge(self, v, u, weight):  # krawedz z v do u
        self.arr[v].append([u, weight])  # tworzymy krotki (u,waga krawedzi z v do u)
        self.edges.append((v, u, weight))

    def printG(self):
        print("\n")
        v = 0
        for i in self.arr:
            print(v, i)
            v += 1
            print("\n")


# relaksacja krawędzi z u do v
def relax(u, v, weight, parent, distance):
    if distance[v] > distance[u] + weight:
        distance[v] = distance[u] + weight
        parent[v] = u


def path(g, s, t):
    # sortujemy krawędzi grafu po wagach krawędzi malejąco
    sorted_edges = sorted(g.edges, key=lambda x: x[2], reverse=True)

    distance = [float("inf")] * g.size
    distance[s] = 0
    parent = [None] * g.size

    for edge in sorted_edges:
        relax(edge[0], edge[1], edge[2], parent, distance)

    # odtwarzamy ścieżkę
    result = []
    idx = t
    while idx is not None:
        result.append(idx)
        idx = parent[idx]

    result.reverse()
    return distance[t], result


G = Graph(6)
G.add_edge(0, 1, 1)
G.add_edge(0, 2, 7)
G.add_edge(1, 3, 2)
G.add_edge(2, 0, 7)
G.add_edge(2, 3, 6)
G.add_edge(2, 4, 10)
G.add_edge(3, 1, 2)
G.add_edge(3, 2, 6)
G.add_edge(3, 4, 5)
G.add_edge(3, 5, 13)
G.add_edge(4, 2, 10)
G.add_edge(4, 3, 5)
G.add_edge(4, 5, 4)
G.add_edge(5, 3, 13)
G.add_edge(5, 4, 4)

print(path(G, 0, 5))
