from collections import deque


# lista sasiedztwa
def BFS(G, s):
    n = len(G)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    queue = deque([s])

    def BFS_visit(u):
        nonlocal G, n, dist, queue
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    while len(queue) > 0:
        BFS_visit(queue.pop())

    return dist


G1 = [[1, 3], [0, 2], [1], [0]]


# macierz sasiedztwa
def BFS2(G, s):
    n = len(G)
    dist = [-1 for _ in range(n)]
    dist[s] = 0
    queue = deque([s])

    def BFS_visit(u):
        nonlocal G, dist, n, queue
        for v in range(n):
            if G[u][v] == 1 and dist[v] == -1:
                dist[v] = dist[u] + 1
                queue.appendleft(v)

    while len(queue) > 0:
        BFS_visit(queue.pop())

    return dist


G2 = [[0,1,0,1],
      [1,0,1,0],
      [0,1,0,0],
      [1,0,0,0]]

print(BFS2(G2,0))