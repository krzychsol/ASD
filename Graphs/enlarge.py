"""
Dany jest graf nieskierowany G = (V, E) oraz dwa wierzchołki s, t ∈ V . Proszę zaproponować i
zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E, której usunięcie
z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algorytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
poprawność i oszacować złożoność obliczeniową.
Algorytm należy zaimplementować jako funkcję:
def enlarge(G, s, t):
...
która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą
warunki zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list
sąsiadów, t.j. G[i] to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0.
Funkcja powinna zwrócić krotkę zawierającą numery dwóch wierzchołków pomiędzy którymi jest
krawędź spełniająca warunki zadania, lub None jeśli takiej krawędzi nie ma. Jeśli w grafie oryginalnie
nie było ścieżki z s do t to funkcja powinna zwrócić None.
"""
"""
Moje rozwiązanie: Wykonujemy 2 razy BFS - z wierzchołka s i t otrzymując odleglosci do wierzcholka s i do wierzcholka t.
Następnie  
"""

from collections import deque
from Graphs.enlarge_tests import runtests

def BFS(G,s):
    n = len(G)
    visited = [False for _ in range(n)]
    dist = [float("inf") for _ in range(n)]
    Q = deque()
    Q.append(s)
    visited[s] = True
    dist[s] = 0

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = min(dist[v],dist[u]+1)
                Q.append(v)

    return dist

def enlarge(G,s,t):
    t1 = BFS(G,s)
    t2 = BFS(G,t)
    n = len(t1)
    dist = t1[t]
    count_dist = [0 for _ in range(dist+1)]
    for i in range(n):
        if t1[i]+t2[i] == dist:
            count_dist[t1[i]] += 1

    goal = None
    for i in range(dist):
        if count_dist[i] == count_dist[i+1] == 1:
            goal = i
            break

    if goal is None:
        return None

    for i in range(n):
        if t1[i] == goal:
            for j in G[i]:
                if t1[j] == t1[i]+1 and t1[j]+t2[j] == dist:
                    return i,j

G = [[1, 2],
    [0, 2],
    [0, 1],]

s = 0
t = 2

runtests(enlarge)