def floyd(G):
    n = len(G)

    for t in range(n):
        for u in range(n):
            for w in range(n):
                G[u][w] = min(G[u][w],G[u][t]+G[t][w])

    return G

G = [[0,5,float("inf"),10],
     [float("inf"),0,3,float("inf")],
     [float("inf"),float("inf"),0,1],
     [float("inf"),float("inf"),float("inf"),0]]

"""
            10
       (0)------->(3)
        |         /|\
      5 |          |
        |          | 1
       \|/         |
       (1)------->(2)
            3           """

S = floyd(G)
for i in range(len(S)):
    print(S[i])