
#sortowanie topologiczne
def DFS(G):
    n = len(G)
    vis = [False] * n
    stack = []

    def DFSVisit(G, u, vis):
        vis[u] = True
        for v,w in G[u]:
            if not vis[v]:
                DFSVisit(G,v,vis)
                stack.append(v)

    for u,w in G[0]:
        if not vis[u]:
            DFSVisit(G,u,vis)
            stack.append(u)

    stack.append(0)
    stack.reverse()
    return stack

G1 = [[(1,3),(3,10)],[(2,3),(3,9)],[(0,1)],[(4,5)],[]]
print(DFS(G1))