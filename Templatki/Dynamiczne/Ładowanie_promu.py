'''
Narazie oblicza ile moze sie zmiescic na jeden pas
samochodów maksymalnie
'''

def prom(A,L):
    n = len(A)
    F = [[0 for _ in range(L+1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = 1

    for j in range(L+1):
        if A[0] == j:
            F[0][j] = 1

    for i in range(1,n):
        for j in range(1,L+1):
            if A[i] > j:
                F[i][j] = F[i-1][j]
            elif A[i] == j:
                F[i][j] = max(1,F[i-1][j])
            else:
                if F[i-1][j-A[i]] != 0:
                    F[i][j] = F[i-1][j-A[i]]+1
                else:
                    F[i][j] = F[i-1][j]

    cnt = F[n-1][L]


A = [3,2,3,4,5,2,3,2]
L = 7

print(prom(A,L))