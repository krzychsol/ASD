class Graph:
    def __init__(self, edges, N):
        self.adjList = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def DFS(graph, v, discovered, parent):
    discovered[v] = True

    for w in graph.adjList[v]:
        if not discovered[w]:
            if DFS(graph, w, discovered, v):
                return True

        elif w != parent:
            return True

    return False

if __name__ == '__main__':

    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)
    ]

    N = 13
    graph = Graph(edges, N)
    discovered = [False] * N

    if DFS(graph, 1, discovered, -1):
        print("Jest cykl")
    else:
        print("Nie ma cyklu")