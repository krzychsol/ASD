import collections


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for ind, val in enumerate(graph[u]):
            if (visited[ind] == False) and (val > 0):
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return visited[t]


def DFS(G, s, visited):
    visited[s] = True
    for i in range(len(G)):
        if G[s][i] > 0 and not visited[i]:
            DFS(G, i, visited)


def edmonds_karp(graph, source, sink):
    n = len(graph)
    org_graph = [i[:] for i in graph]
    parent = [-1] * len(graph)
    max_flow = 0
    while bfs(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    visited = [False for _ in range(n)]
    DFS(graph, source, visited)
    edges = []
    min_cut_sum = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and org_graph[i][j] > 0 and visited[i]:
                min_cut_sum += org_graph[i][j]
                edges.append((i, j))

    return min_cut_sum, edges


def sabotage(G, s, t):
    return edmonds_karp(G, s, t)


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

src = 0
sink = 5
print(sabotage(graph, src, sink))
