from zad5ktesty import runtests

def garek ( A ):
    n = len(A)
    F = [[(0,0) for _ in range(n)] for __ in range(n)]

    for i in range(n):
        F[i][i] = (A[i],0)

    for i in range(n-1):
        F[i][i+1] = (max(A[i],A[i+1]),min(A[i],A[i+1]))

    for i in range(n-3,-1,-1):
        for j in range(i+2,n):
            if A[i]+F[i+1][j][1] > A[j]+F[i][j-1][1]:
                F[i][j] = (A[i]+F[i+1][j][1], F[i+1][j][0])
            else:
                F[i][j] = (A[j]+F[i][j-1][1],F[i][j-1][0])

    return F[0][n-1][0]

#T = [8,15,3,7]
#print(garek(T))
runtests ( garek )