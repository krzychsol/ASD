def DFS(G, s):
    time = [-1] * len(G)
    visited = [False] * len(G)
    t = 1

    def DFSVisit(u):
        nonlocal G, time, t, visited
        time[u] = t
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                DFSVisit(v)
                time[v] = t
                t += 1
    DFSVisit(s)
    return time

def DFS2(G,s,time):
    def DFS2Visit(u):
        nonlocal G, time
        time[u] *= -1
        print(u)
        for v in G[u]:
            if time[v] < 0:
                DFS2Visit(v)
    DFS2Visit(s)

def SCC(G,s):
    time = DFS(G, s)
    revG = [[]for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            revG[G[i][j]].append(i)

    while 1:
        mini = 0
        idx = 0
        for i in range(len(time)):
            if mini > time[i]:
                mini = time[i]
                idx = i
        if mini == 0:
            break
        DFS2(revG,idx,time)
        print("\n")
    return revG

G = [[1,2],[2],[3],[5],[2,6],[4],[]]
print(SCC(G, 0))
