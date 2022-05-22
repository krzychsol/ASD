# szukanie cyklu Eulera w grafie (spójnym!)
# DFS, z tą różnicą, że odznaczamy krawędzi, po których przeszliśmy (a nie wierzchołki)
# gdy odwiedzimy już wszystkich sąsiadów danego wierzchołka, to dodajemy go do cyklu
# oznaczamy krawędzie jako odwiedzone wpsiując 2 zamiast 1 w oryginalnym grafie

def euler(G):

    #dla grafu nieskierowanego musza byc tylko parzyste stopnie wierzchołków
    n = len(G)
    for vertex in range(n):
        degree = sum(G[vertex])
        if degree%2 == 1:
            return None

    order = []
    def DFSvisit(u):
        for v in range(n):
            if G[u][v] == 1:
                G[u][v] = G[v][u] = 2
                DFSvisit(v)
        order.append(u)

    # graf jest nieskierowany oraz spójny, więc po 1 wywołaniu cały graf zostanie odwiedzony
    DFSvisit(0)
    return order


# macierzowa reprezentacja grafu
G = [[0, 1, 0, 0, 0, 1],
       [1, 0, 1, 1, 0, 1],
       [0, 1, 0, 1, 0, 0],
       [0, 1, 1, 0, 1, 1],
       [0, 0, 0, 1, 0, 1],
       [1, 1, 0, 1, 1, 0]]

print(euler(G))