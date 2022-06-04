'''
Przewodnik chce przewieźć grupę turystów z miasta A do miasta B. Po drodze jest
jednak wiele innych miast i między różnymi miastami jeżdzą autobusy o różnej pojemności.
Mamy daną listę trójek postaci (x, y, c), gdzie x i y to miasta między którymi bezpośrednio
jeździ autobus o pojemności c pasażerów. Proszę zaproponować algorytm, który znajduje trasę
z A do B, po której może przejechać możliwie jak największa grupa turystów bez rozdzielania się.
'''

# ALGORYTM:

# 1. używamy algorytmu podobnego do Dijkstry, z tym, że używamy kolejki priorytetowej typu max
#    a "relaksacja" krawędzi z u do v polega na tym, że bierzemy minimum z [wagi krawędzi] oraz
#    [większej z wag przypisanych do wierchołków u i v], dzięki czemu weźmiemy największą z możliwych
#    dostępnych pojemności - czyli szukaną liczebność grupy

# 2. szukamy "maksymalnego" drzewa rozpinającego - jego krawędź o najmniejszej wadze to szukana grupa

# 3. BISEKCJA+DFS
#    sortujemy po długościach krawędzie rosnąco, biorę jako przypuszczalnie szukaną wartość środkową i
#    i nie biorąc pod uwagę krawędzi o mniejszej wadze, puszcam DFS i sprawdzam czy zdoła on
#    odwiedzić miasto B. Jeśli tak, to sprawdzam wartość będącą w połowie stawki powyżej wziętej
#    poprzednio krawędzi, analogicznie jeśli nie - poniżej.


# sposób nr 2 - korzystamy z algorytmu analogicznego do algorytmu Prima, tylko bierzemy krawędzi
# o maksymalnych wagach

# ponieważ korzystamy z kolejki priorytetowej o priorytecie min, to aby wyciągać krawędzi o
# maksymalnych wagach dokonujemy modyfikacji - wstawiamy do kolejki wagi przeciwne (minus)
# i ignorujemy wartości inf

from queue import PriorityQueue


class Graph:
    def __init__(self, size):
        self.size = size
        self.arr = [[i] for i in range(size)]

    def add_edge(self, v, u, weight):  # krawędź z v-u
        self.arr[v].append((weight, u))
        self.arr[u].append((weight, v))

    def printG(self):
        print("\n")
        for i in self.arr:
            for j in i:
                print(j, end=" ")
            print("\n")


def MSTPrim(G, s):
    n = G.size
    visited = [False for _ in range(n)]
    Q = PriorityQueue()
    for i in range(n):
        if i != s:
            Q.put((float("inf"), i))
    Q.put((0, s))

    max_weight = [float("-inf ") for _ in range(n)]
    max_weight[s] = 0
    parent = [None for _ in range(n)]

    while not Q.empty():
        _, u = Q.get()
        visited[u] = True
        for v in G.arr[u][1:]:
            if not visited[v[1]]:
                # aktualizuję wagi
                if v[0] != float("inf") and max_weight[v[1]] < v[0]:
                    max_weight[v[1]] = v[0]
                    parent[v[1]] = u
                    Q.put((-1 * v[0], v[1]))

    return parent


def tour(G, v, s, t):
    newG = Graph(v)
    for edge in G:
        newG.add_edge(edge[0], edge[1], edge[2])

    parents = MSTPrim(newG, s)
    path = []
    idx = t
    while idx != None:
        path.append(idx)
        idx = parents[idx]

    path.reverse()
    return path


G = [[0, 1, 70], [0, 3, 100], [1, 2, 60], [1, 3, 20], [2, 3, 2], [2, 4, 80], [3, 4, 40]]

print(tour(G, 5, 0, 4))
