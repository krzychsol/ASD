# Krzysztof Solecki
"""
Algorytm szuka cyklu Hamiltona w zadanym grafie i jeśli istnieje to zwraca kolejność wierzchołków (miast) na ścieżce cyklu.
W tym celu wykonuje algorytm DFS z wierzchołka 0 i bramy północnej (wybór początkowej bramy i wierzchołka nie ma znaczenia dla wyniku algorytmu,
ponieważ graf jest nieskierowany oraz jeśli istnieje cykl Hamiltona, przechodzący przez każdy wierzchołek i każdą bramę dokładnie raz to jest on osiągalny z każdego punktu startowgo).
Przy odwiedzaniu wierzchołka wrzucam go na stos i sprawdzam czy wielkość stosu jest równa ilości wierzchołków oraz czy z ostatniego odwiedzonego wierzchołka
istnieje krawędź do wierzchołka 0 i bramy północnej. Jeśli tak to zwracam wynik jeśli nie to kontynuuje algorytm.
Złożoność czasowa: O(V!) - mogę wielokrotnie odwiedzać ten sam wierzchołek
Złożoność pamięciowa: O(V)
"""

from zad7testy import runtests


def DFS(G, s, src_side):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(u, stack, side, stack_len):
        nonlocal G, n, visited, s, src_side
        stack.append(u)
        stack_len += 1

        if stack_len == n:
            for v in G[u][1 - side]:
                if v == s and u in G[s][src_side]:
                    return stack
        else:
            visited[u] = True

            for v in G[u][1 - side]:
                if not visited[v]:
                    if u in G[v][side]:
                        res = DFS_visit(v, stack, side, stack_len)
                    else:
                        res = DFS_visit(v, stack, 1 - side, stack_len)
                    if res is not None:
                        return res

            visited[u] = False
        stack.pop()
        stack_len -= 1
        return None

    return DFS_visit(s, [], src_side, 0)


def droga(G):
    return DFS(G, 0, 0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(droga, all_tests=True)
