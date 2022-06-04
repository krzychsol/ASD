import copy, collections

def BFS(G, s, t, parent):
    n = len(G)
    visited = [False] * n
    queue = collections.deque()
    queue.append(s)
    visited[s] = True
    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and G[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[t]

def edmonds_karp(G, src, sink):
    parent = [-1] * len(G)
    max_flow = 0
    while BFS(G, src, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != src:
            path_flow = min(path_flow, G[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != src:
            u = parent[v]
            G[u][v] -= path_flow
            G[v][u] += path_flow
            v = parent[v]
    return max_flow


def maxflow(G, s):
    n = len(G)
    v = 0
    for i in range(n):
        v = max(v, G[i][0], G[i][1])
    v += 1

    NG = [[0 for _ in range(v)] for __ in range(v)]
    for i in range(n):
        NG[G[i][0]][G[i][1]] = G[i][2]

    flow = 0
    for el in NG:
        print(el)
    for i in range(v):
        for j in range(v):
            if i == j or i == s or j == s: continue
            flow_i = edmonds_karp(NG,s,i)
            flow_j = edmonds_karp(NG,s,j)
            print(i,flow_i)
            print(j,flow)

    return flow


# zmien all_tests na True zeby uruchomic wszystkie testy
G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
(3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)]
s = 2
print(maxflow(G,s))
#runtests( maxflow, all_tests = False )