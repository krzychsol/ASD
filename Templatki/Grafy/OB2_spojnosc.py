class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, discovered):
    discovered[v] = True

    for u in graph.adjList[v]:
        if not discovered[u]:
            DFS(graph, u, discovered)

    print(v,end=" ")

if __name__ == '__main__':

    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)]

    N = 13
    graph = Graph(edges, N)
    discovered = [False] * N

    for i in range(N):
        if not discovered[i]:
            DFS(graph, i, discovered)