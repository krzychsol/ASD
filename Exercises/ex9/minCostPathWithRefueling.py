"""
Zadanie 7. (problem stacji benzynowych na grafie) Pewien podróżnik chce przebyć trasę z punktu A
do punktu B. Niestety jego samochód spala dokładnie jeden litr paliwa na jeden kilometr trasy. W baku mieści
się dokładnie D litrów paliwa. Trasa jest reprezentowana jako graf, gdzie wierzchołki to miasta a krawędzie to
łączące je drogi. Każda krawędź ma długość w kilometrach (przedstawioną jako licza naturalna). W każdym
wierzchołku jest stacja benzynowa, z daną ceną za litr paliwa. Proszę podać algorytm znajdujący trasę z
punktu A do punktu B o najmniejszym koszcie. Proszę uzasadnić poprawność algorytmu.

Opis: Robijamy każdy wierzchołek na D wierzchołków. W praktyce jest to dynamik na grafie gdzie
graph[i][j] - minimalny koszt dojechania do wierzchołka i mając j litrow paliwa w momencie dotarcia do
tego wierzchołka.
"""

from math import inf
from queue import PriorityQueue


def relax(G, u, v, dist, cost):
    capacity = len(G[u])
    for i in range(dist, capacity):
        for j in range(i - dist, capacity):
            G[v][j] = min(G[v][j], G[u][i] + j * cost)


def cheapest_trip_with_refueling(G, city_a, city_b, capacity):
    n = len(G)
    new_G = [[inf for _ in range(capacity + 1)] for __ in range(n)]
    visited = [False for _ in range(n)]
    for i in range(capacity + 1):
        new_G[city_a][i] = G[city_a][1] * i
    Q = PriorityQueue()
    Q.put((0, city_a))

    while not Q.empty():
        dist, u = Q.get()
        visited[u] = True
        for v, weight in G[u][0]:
            if not visited[v] and weight <= capacity:
                relax(new_G, u, v, weight, G[v][1])
                Q.put((new_G[v][weight],v))

    return new_G[city_b][0]


G = [[[(1, 4), (3, 6)], 1],
     [[(0, 4), (2, 7), (3, 5)], 2],
     [[(1, 7), (4, 10)], 4],
     [[(0, 6), (1, 5), (4, 3), (5, 10)], 5],
     [[(2, 10), (3, 3), (5, 4)], 3],
     [[(3, 10), (4, 4)], 0]]
print(cheapest_trip_with_refueling(G, 0, len(G) - 1, 15))
