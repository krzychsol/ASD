"""
Zadanie 1. (ścieżka Hamiltona w DAGu) Ścieżka Hamiltona to ścieżka przechodząca przez wszystkie
wierzchołki w grafie, przez każdy dokładnie raz. W ogólnym grafie znalezienie ścieżki Hamiltona jest problemem NP-trudnym. Proszę podać algorytm, który stwierdzi czy istnieje ścieżka Hamiltona w acyklicznym
grafie skierowanym.
"""
"""
Sortuje DAG topologicznie, w momencie odwiedzania wierzchołka
odkładam go na stos i sprawdzam czy z wierzchołka przedostatniego na stosie jest
krawędz do tego. Jeśli nie ma to nie ma ścieżki Hamiltona.
"""


def hamilton_in_DAG(G):
    n = len(G)
    visited = [False for _ in range(n)]
    stack = []
    stack_len = 0

    def DFS_visit(u):
        nonlocal G, n, visited, stack,stack_len
        stack.append(u)
        stack_len += 1
        if stack_len >= 2:
            a = stack[stack_len-2]
            b = stack[stack_len-1]
            if not G[a][b]:
                return False

        visited[u] = True
        for v in range(n):
            if G[u][v] and not visited[v]:
                res = DFS_visit(v)
                if not res:
                    return None
        return stack

    return DFS_visit(0)


G = [[0,1,0,0],
     [0,0,1,1],
     [0,0,0,0],
     [0,0,0,0]]

print(hamilton_in_DAG(G))

