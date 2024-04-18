# The internet cafe has K computers and A applications on CDs. Maximum one application can be installed
# on each computer. Each application has a list of computers on which it can run and the rest cannot, due
# to hardware requirements. We are the owner of a cafe and we know haw many customers (possibly zero) will
# would like to use the application tomorrow. We assume that each client occupies a computer for the
# whole day. What an application should we install on each of the computers so that all customers can use
# the application which they want. If there is not such an assignment, the algorithm should consider that.


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


def edmonds_karp(graph, source, sink):
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
    return max_flow


def coffee_point(G, computers, applications, demand_apps):
    k = len(computers)
    a = len(applications)
    d = len(demand_apps)
    size = k + a + 2
    new_G = [[0 for _ in range(size)] for __ in range(size)]

    for i in range(a):
        for j in range(len(G[applications[i]])):
            new_G[applications[i] + 1][G[applications[i]][j] + 1] = 1

    for i in range(k):
        new_G[computers[i] + 1][-1] = 1

    customers = 0
    for i in range(d):
        customers += demand_apps[i][1]
        new_G[0][demand_apps[i][0]+1] = demand_apps[i][1]

    result = edmonds_karp(new_G, 0, size - 1)
    if result == customers:
        return True
    return False


applications = [0, 1, 2, 3]
computers = [4, 5, 6, 7, 8]
demand_applications = [(0, 2), (1, 2), (3, 1)]
graph = [[4, 7], [5, 6, 7], [4, 7], [8]]
print(coffee_point(graph, computers, applications, demand_applications))
