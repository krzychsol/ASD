class Street:
    def __init__(self):
        self.u = None
        self.v = None
        self.len = None

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def darkRoads(G,n,m):
    groups = [0] * m
    streetCnt = 0
    originalCost = 0
    cost = 0
    for i in range(m):
        originalCost += G[i][2]

    G = sorted(G, key=lambda x: x[2])
    for i in range(m):
        groups[i] = i

    for i in range(len(G)):
        if streetCnt >= m - 1:
            break
        groupU = find(groups, G[i][0])
        groupV = find(groups, G[i][1])
        if groupU != groupV:
            cost += G[i][2]
            groups[groupV] = groupU
            streetCnt += 1

    return originalCost-cost

n = 7
m = 11
G = [(0,1,7),
     (0,3,5),
     (1,2,8),
     (1,3,9),
     (1,4,7),
     (2,4,5),
     (3,4,15),
     (3,5,6),
     (4,5,8),
     (4,6,9),
     (5,6,11)]

print(darkRoads(G,n,m))