# There are traffic jams in Cracow during rush hours. Therefore drivers are more concerned with time than
# with the real distance between two points. We are given a map of Cracow, distances and travel times are
# marked between road intersections. There are one-way streets and two-way streets in Cracow. Drivers need
# an app to help them find the roads that allow them to get from intersection A to B in the shortest
# possible time and among those with the shortest time it selects and returns the shortest in terms of
# distance. We have to process Q queries represented as (intersectionA, intersectionB) and answer each of
# them with a pair (time, distance) of the best way. All queries refer to the same graph.
# What solution gives the best complexity in each of the following cases?
#   1) Q = O(1), E = O(V)
#   2) Q = O(1), E = O(V^2)
#   3) Q = O(V), E = O(V)
#   4) Q = O(V), E = O(V^2)

# Solution:
# 1) Dijkstra algorithm will have complexity O(V^2*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Dijkstra algorithm.
# 2) Dijkstra algorithm will have complexity O(V^3*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Floyd-Warshall algorithm.
# 3) Dijkstra algorithm will have complexity O(V^2*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Dijkstra algorithm.
# 4) Dijkstra algorithm will have complexity O(V^3*log(V)).
#    Floyd-Warshall algorithm will have complexity O(V^3).
#    The better choice in this case is Floyd-Warshall algorithm.
# We can see that for sparse graph (1 and 3 cases) the better choice in this exercise is Dijkstra algorithm,
# but for dense graph (2 and 4 cases) the better option is to use Floyd-Warshall algorithm.

from queue import PriorityQueue


def cracow_traffic(G, a, b):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    time = [float("inf") for _ in range(n)]
    dist[a] = 0
    time[a] = 0
    Q = PriorityQueue()
    for i in range(n):
        if i != a:
            Q.put((float("inf"), float("inf"), i))
    Q.put((0, 0, a))  # czas,odleglosc,wierzcholek

    while not Q.empty():
        _, _, u = Q.get()
        visited[u] = True
        for v, c, d in G[u]:
            if not visited[v]:
                if time[v] > time[u] + c:
                    time[v] = time[u] + c
                    dist[v] = dist[u] + d
                    parent[v] = u
                elif time[v] == time[u] + c:
                    if dist[v] > dist[u] + d:
                        dist[v] = dist[u] + d
                        parent[v] = u

    print(time[b], dist[b])


G = [[(1, 1, 7), (2, 5, 10)],
     [(0, 1, 7), (3, 3, 7)],
     [(0, 5, 10), (4, 2, 5)],
     [(1, 3, 7), (5, 3, 10)],
     [(2, 2, 5), (5, 1, 4)],
     [(3, 3, 10), (4, 1, 4)]]

cracow_traffic(G, 0, 5)
