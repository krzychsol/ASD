def subsetsum(A,T):
    n = len(A)
    F = [[False for _ in range(T+1)] for _ in range(n+1)]

    for i in range(n+1):
        F[i][0] = True

    for i in range(1,n+1):
        for j in range(1,T+1):
            if A[i-1] > j:
                F[i][j] = F[i-1][j]
            else:
                F[i][j] = F[i-1][j] or F[i-1][j-A[i-1]]

    return F[n][T]

A=[4,7,8,13,2]
T = 10
print(subsetsum(A,T))