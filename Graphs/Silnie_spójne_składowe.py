def DFS(G, u, visited, result, idx):
    visited[u] = True
    result[idx].append(u)
    for v in G[u]:
        if not visited[v]:
            DFS(G, v, visited, result, idx)


def transpose_graph(G, newG):
    for u in range(len(G)):
        for v in range(len(G[u])):
            newG[G[u][v]].append(u)


def DFSUtil(G, u, visited, stack):
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFSUtil(G, v, visited, stack)
    stack.append(u)


def SCC(G):
    n = len(G)
    visited = [False for _ in range(n)]
    stack = []
    for u in range(n):
        if not visited[u]:
            DFSUtil(G, u, visited, stack)

    new_graph = [[] for _ in range(n)]
    transpose_graph(G, new_graph)
    visited = [False for _ in range(n)]
    result = [[] for _ in range(n)]
    idx = 0
    while len(stack) > 0:
        u = stack.pop()
        if not visited[u]:
            DFS(G, u, visited, result, idx)
            idx += 1
    return result


graph = [[1,2],[],[1,3],[],[3,5],[3]]
print(SCC(graph))