def printsolution(reach,n):
    for i in range(n):
        for j in range(n):
            print(reach[i][j],end=" ")
        print("\n")

def TransitiveClousure(G):
    n = len(G)
    reach =[i[:] for i in G]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])

    printsolution(reach,n)

G = [[1, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]]

TransitiveClousure(G)


