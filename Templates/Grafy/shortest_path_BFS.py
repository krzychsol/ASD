class Graph:
    def __init__(self,edges,N):
        self.adjList = [[] for _ in range(N)]

        for (src,dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

def BFS_SP(graph, start, goal):
    explored = []
    queue = []

    if start == goal:
        return start

    while queue:
        path = queue.pop(0)
        v = path[-1]

        if v not in explored:
            for u in graph.adjList[v]:
                new_path = list(path)
                new_path.append(u)
                queue.append(new_path)

                if u == goal:
                    return new_path
            explored.append(v)

    return None

edges = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12)]

N = 15
graph = Graph(edges,N)

print(BFS_SP(graph,1,7))