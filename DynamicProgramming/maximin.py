"""
Zadanie 5. (maximin) Rozważmy ciąg (a0, . . . , an−1) liczb naturalnych. Załóżmy, że został podzielony
na k spójnych podciągów: (a0, . . . , a`1), (a`1+1, . . . , a`2), . . . , (a`k−1+1, . . . , an−1).
Przez wartość i-go podciągu rozumiemy sumę jego elementów a przez najgorszy podciąg rozumiemy podciąg o najmniejszej wartości
(rozstrzygając remisy w dowolny sposób). Wartością podziału jest wartość jego najgorszego podciągu. Zadanie
polega na znalezienie podziału ciągu (a0, . . . , an−1) o maksymalnej wartości.
"""
# F(i,k) - maksymalna wartość podziału rozwazajac do i-tego elementu i dzielac na k czesci

def maximin(A,k):
    n = len(A)
    F = [[0 for _ in range(k+1)] for __ in range(n+1)]

    #dla n = 1
    for i in range(1,k+1):
        F[1][i] = A[0]

    #dla k = 1
    for i in range(1,n+1):
        F[i][1] = sum(A[:i])

    #dla k od 2 do n
    for i in range(2,k+1):
        for j in range(2,n+1):
            best = float("inf")
            for p in range(1,j+1):
                best = min(best,max(sum(A[p:j]),F[p][i-1]))
            F[j][i] = best

    return F[n][k]

A = [10,15,15,70,40,40]
k = 3
print(maximin(A,k))