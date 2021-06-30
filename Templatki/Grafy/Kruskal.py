def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot

    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def KruskalMST(G,V):
    n = len(G)
    res = []
    i = 0
    e = 0
    G = sorted(G,key=lambda x:x[2])
    parent = []
    rank = []

    for v in range(n):
        parent.append(v)
        rank.append(0)

    while e < V-1:
        u,v,w = G[i]
        i+=1
        x = find(parent,u)
        y = find(parent,v)
        if x != y:
            e += 1
            res.append([u,v,w])
            union(parent,rank,x,y)

    minCost = 0
    for u,v,w in res:
        minCost += w
        print("%d -- %d == %d" % (u, v, w))
    print(minCost)

G = [[0,1,10],[0,2,6],[0,3,5],[1,3,15],[2,3,4]]
V = 4
KruskalMST(G,V)