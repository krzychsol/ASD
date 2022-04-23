"""
Zadanie 3. (najdłuższy wspólny podciąg) Mamy dane dwie tablice,
A[n] i B[n]. Należy znaleźć długość ich najdłuższego wspólnego podciągu.
(Klasyczny algorytm dynamiczny O(n^2))
"""
#O(mn)

def LCS(X,Y):
    m = len(X)
    n = len(Y)
    curr = [None for _ in range(n+1)]

    for i in range(m+1):
        prev = curr[0]
        for j in range(n+1):
            current = curr[j]
            if i == 0 or j == 0:
                curr[j] = 0
            else:
                if X[i-1] == Y[j-1]:
                    curr[j] = prev+1
                else:
                    curr[j] = max(curr[j],curr[j-1])
            prev = current

    return curr[n]