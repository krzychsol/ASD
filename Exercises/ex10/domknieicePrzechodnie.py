"""
Alogrytm oblicza domknięcie przechodnie grafu skierowanego.
Dla nieskierowanego można też wykorzystać silnie spójne składowe.
"""


def transitiveClousure(G):
    n = len(G)
    TC = G.copy()

    for u in range(n):
        for v in range(n):
            for k in range(n):
                if G[u][k] and G[k][v] or G[u][v]:
                    TC[u][v] = 1
    return TC


G = [[0, 1, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0]]

transitiveClousure(G)
