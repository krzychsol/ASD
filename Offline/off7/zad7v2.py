# Krzysztof Solecki
"""
Algorytm szuka cyklu Hamiltona w zadanym grafie i jeśli istnieje to zwraca kolejność wierzchołków (miast) na ścieżce cyklu.
W tym celu wykonuje algorytm DFS z wierzchołka 0 i bramy północnej (wybór początkowej bramy i wierzchołka nie ma znaczenia dla wyniku algorytmu,
ponieważ graf jest nieskierowany oraz jeśli istnieje cykl Hamiltona, przechodzący przez każdy wierzchołek i każdą bramę dokładnie raz to jest on osiągalny z każdego punktu startowgo).
Przy odwiedzaniu wierzchołka wrzucam go na stos i sprawdzam czy wielkość stosu jest równa ilości wierzchołków oraz czy z ostatniego odwiedzonego wierzchołka
istnieje krawędź do wierzchołka 0 i bramy północnej. Jeśli tak to zwracam wynik jeśli nie to kontynuuje algorytm.

Złożoność czasowa: O(V! * 2^V), ponieważ sprawdzam wszystkie możliwe podzbiory wierzchołków.
Złożoność pamięciowa: O(V)
"""

from zad7testy import runtests



def preprocessing(G):
    n = len(G)
    edges = 0
    for u in range(n):
        for v in G[u][0]:
            if v > u:
                edges += 1
        for v in G[u][1]:
            if v > u:
                edges += 1

    newG = [[] for _ in range(edges)]


def droga(G):
    newG = preprocessing(G)


# G = [([],[1,2]),([0],[2]),([0],[1])]
# print(droga(G))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=False)
