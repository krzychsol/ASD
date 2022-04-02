"""
Zadanie 2. (problem sumy podzbioru) Dana jest tablica n liczb naturalnych A.
Proszę podać i zaimplementować algorytm, który sprawdza, czy da się
wybrać podciąg liczb z A, które sumują się do zadanej wartości T
"""


def subsetsum(A, T):
    n = len(A)
    F = [[False for _ in range(T + 1)] for __ in range(n + 1)]

    for i in range(n + 1):
        F[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, T + 1):
            if A[i-1] > j:
                F[i][j] = F[i - 1][j]
            else:
                F[i][j] = F[i - 1][j] or F[i - 1][j - A[i-1]]

    return F[n][T],F

def getsolution(F,A,T,i,j):
    if (T == 0 and j==0) or i == 0:
        return []

    if A[i-1] <= j and F[i][j] == F[i-1][j-A[i-1]]:
        return getsolution(F,A,T-A[i-1],i-1,j-A[i-1])+[i-1]

    return getsolution(F,A,T,i-1,j)



A = [1,2,7,8,9]
T = 9
result,F = subsetsum(A,T)
i = len(A)
if result:
    print(getsolution(F,A,T,i,T))
else:
    print(result)
