"""
Zadanie 4. (mnożenie macierzy) Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
koszt mnożenia przy optymalnym doborze kolejności.
"""
#O(n^2)


def matrixChainOrder(p,n):
    # For simplicity of the program, one
    # extra row and one extra column are
    # allocated in dp[][]. 0th row and
    # 0th column of dp[][] are not used
    dp = [[0 for i in range(n)]
          for i in range(n)]

    # dp[i, j] = Minimum number of scalar
    # multiplications needed to compute
    # the matrix M[i]M[i+1]...M[j] = M[i..j]
    # where dimension of M[i] is p[i-1] x p[i]

    # cost is zero when multiplying one matrix.
    for i in range(1, n):
        dp[i][i] = 0

    for length in range(1,n-1):
        for i in range(n-length):
            dp[i][i+length] = min(dp[i+1][i+length]+p[i-1]*p[i]*p[i+length],dp[i][i+length-1]+p[i-1]*p[i+length-1]*p[i+length])

    return dp[1][n-1]

P = [5,10,3,12,5,50,6]
n = len(P)
print(matrixChainOrder(P,n))