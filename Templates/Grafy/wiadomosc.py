from collections import deque

class Graph:
    def __init__(self,edges,N):
        self.adj = [[] for _ in range(N)]

        for (src,dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def BFS(graph,s,discovered,waves,parents):
    q = deque()
    discovered[s] = True
    q.append(s)
    waves[s] = 0

    while q:
        v = q.popleft()
        for u in graph.adj[v]:
            if not discovered[u]:
                discovered[u] = True
                waves[u] = waves[v]+1
                parents[u] = v
                q.append(u)

    return waves

if __name__ == '__main__':

    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)
    ]

    N = 13
    graph = Graph(edges, N)
    discovered = [False] * N
    waves = [-1]*len(graph.adj)
    parents=[-1]*len(graph.adj)

    freq = BFS(graph,1,discovered,waves,parents)
    C = [0]*(max(freq)+2)
    midx = -1

    for i in range(len(freq)):
        if C[freq[i]]+1 > max(C):
            midx = freq[i]
        C[freq[i]]+=1

    print("Dzien w kotrym najwiecej wiadomosci dotarlo: ",midx+1)
    print("Ilosc wiadomosci tego dnia: ",max(C))