# Algorytm weryfikuje istnienie cyklu w grafie

def CycleDetection(G):
    n = len(G)
    visited = [False for _ in range(n)]

    def DFS_visit(u, parent):
        nonlocal visited, G, n
        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                return DFS_visit(v, u)
            elif v != parent:
                return True
        return False

    return DFS_visit(0, None)


G = [[1, 2], [0, 2], [1, 3], [2]]
print(CycleDetection(G))
