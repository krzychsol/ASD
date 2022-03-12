from EGZAMIN20.Termin2.zad1testy import runtests
from math import inf

def zbigniew(A):
    n = len(A)
    energy = sum(A)+n
    F = [[inf for _ in range(energy+1)] for _ in range(n)]
    F[0][A[0]] = 0
    for x in range(1, n):
        for y in range(energy+1 - n):
            if y >= A[x]:
                for i in range(x-1, -1, -1):
                    if F[i][y-A[x]+(x-i)] + 1 < F[x][y]:
                        F[x][y] = F[i][y-A[x]+(x-i)] + 1
    for i in range(n):
        print(F[i])
    return min(F[n-1])

runtests( zbigniew ) 
