from collections import deque

V = 9
class node:
    def __init__(self, to, weight):
        self.to = to
        self.weight = weight

edges = [0] * V
for i in range(V):
    edges[i] = []

def BFS(src,dest):
    dist = [0] * V
    for i in range(V):
        dist[i] = float('inf')

    Q = deque()
    dist[src] = 0
    Q.append(src)

    while Q:
        v = Q.popleft()

        for i in range(len(edges[v])):

            if dist[edges[v][i].to] > dist[v] + edges[v][i].weight:
                dist[edges[v][i].to] = dist[v] + edges[v][i].weight

                if edges[v][i].weight == 0:
                    Q.appendleft(edges[v][i].to)
                else:
                    Q.append(edges[v][i].to)

    return dist[dest]

def addEdge(u: int, v: int, wt: int):
    edges[u].append(node(v, wt))
    edges[u].append(node(v, wt))

if __name__ == "__main__":
    addEdge(0, 1, 0)
    addEdge(0, 7, 1)
    addEdge(1, 7, 1)
    addEdge(1, 2, 1)
    addEdge(2, 3, 0)
    addEdge(2, 5, 0)
    addEdge(2, 8, 1)
    addEdge(3, 4, 1)
    addEdge(3, 5, 1)
    addEdge(4, 5, 1)
    addEdge(5, 6, 1)
    addEdge(6, 7, 1)
    addEdge(7, 8, 1)

    src = 0
    dest = 6
    print(BFS(src,dest))
