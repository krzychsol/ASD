''' Dany jest ciąg przedziałów postaci [ai, bi]. Dwa przedziały można
skleić jeśli mają dokładnie jeden punkt wspólny. Proszę wskazać algorytm dla następującego problemu:

1. Problem stwierdzenia, czy da się uzyskąć przedział [a, b] przez sklejanie odcinków.
'''


def stick(arr, a, b):
    vtx = 0
    n = len(arr)
    for i in range(len(arr)):
        for j in arr[i]:
            vtx = max(vtx, j)

    G = [[0 for _ in range(vtx)] for __ in range(vtx)]
    for i in range(n):
        G[arr[i][0]-1][arr[i][1]-1] = G[arr[i][1]-1][arr[i][0]-1] = 1

    for el in G:
        print(el)

    def DFS(G):
        nonlocal a, b
        n = len(G)
        visited = [False] * n

        def DFSvisit(u):
            visited[u] = True
            for v in range(n):
                if G[u][v] and not visited[v]:
                    visited[v] = True
                    DFSvisit(v)

        DFSvisit(a-1)
        return visited[b-1]

    return DFS(G)


arr = [[1, 3], [2, 4], [3, 5], [5, 7], [6, 8], [7, 9]]
print(stick(arr, 5, 4))
