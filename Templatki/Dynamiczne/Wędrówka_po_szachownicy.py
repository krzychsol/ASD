#mozna poruszac sie w prawo i w dół

def findMinCost(C):
    (M,N) = (len(C),len(C[0]))
    T = [[0 for _ in range(N)] for _ in range(M)]

    for i in range(M):
        for j in range(N):
            T[i][j] = C[i][j]

            if i == 0 and j > 0:
                T[0][j] += T[0][j-1]
            elif j == 0 and i > 0:
                T[i][0] += T[i-1][0]
            elif i > 0 and j > 0:
                T[i][j] += min(T[i-1][j],T[i][j-1])

    return T[M-1][N-1]
