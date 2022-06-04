def isSafe(G, v, pos, path):
    if not path[0] in G[path[pos-1]]:
        return False
    for vertex in path:
        if vertex == v:
            return False

    return True


def hamCycleUtil(G, path, pos):
    n = len(G)
    if pos == n:
        if path[0] in G[path[pos-1]]:
        #if G[path[pos - 1]][path[0]] == 1:
            return True
        else:
            return False

    for v in range(1, n):
        if isSafe(G, v, pos, path):
            path[pos] = v
            if hamCycleUtil(G, path, pos + 1):
                return True
            path[pos] -= 1
    return False


def hamCycle(G,s):
    n = len(G)
    path = [-1 for _ in range(n)]
    path[0] = s
    if not hamCycleUtil(G, path, 1):
        return None

    return path


G2 = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],
            [0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],
            [0, 1, 1, 1, 0], ]



G = [([1], [2, 3, 4]),
     ([0], [2, 5, 6]),
     ([1, 5, 6], [0, 3, 4]),
     ([0, 2, 4], [5, 7, 8]),
     ([0, 2, 3], [6, 7, 9]),
     ([1, 2, 6], [3, 7, 8]),
     ([1, 2, 5], [4, 7, 9]),
     ([4, 6, 9], [3, 5, 8]),
     ([3, 5, 7], [9]),
     ([4, 6, 7], [8])]

print(hamCycle(G,0))