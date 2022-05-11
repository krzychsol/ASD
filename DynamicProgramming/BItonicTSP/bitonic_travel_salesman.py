from math import sqrt

def d(i, j, tab, D):  # odległośći
    if D[j][i] > 0:
        return D[j][i]
    else:
        return sqrt((tab[i][2] - tab[j][2]) ** 2 + (tab[i][1] - tab[j][1]) ** 2)


def tspf(i, j, F, D):
    if F[i][j] != float("inf"):
        return F[i][j]

    if i == j - 1:
        best = float("inf")
        for k in range(j - 1):
            best = min(best, tspf(i, j - 1, F, D) + D[k][j])
        F[i][j] = best

    else:
        F[i][j] = tspf(i, j - 1, F, D) + D[j - 1][j]
    return F[i][j]


def bitonicTSP(C):
    n = len(C)
    D = [[-1 for _ in range(n)] for __ in range(n)]
    F = [[float("inf") for _ in range(n)] for __ in range(n)]

    C = sorted(C, key=lambda x: x[1])

    for i in range(n):
        for j in range(n):
            D[i][j] = d(i,j,C,D)

    F[0][1] = D[0][1]
    m = tspf(0,n-1,F,D)+D[0][n-1]


C = [["Wrocław", 0, 2], ["Warszawa",4,3],
["Gdańsk", 2,4], ["Kraków",3,1]]

bitonicTSP(C)
