"""(wędrówka po szachownicy) Dana jest szachownica A o wymiarach n × n. Szachownica
zawiera liczby calkowite. Należy przejść z pola (1, 1) na pole (n, n) korzystając jedynie z ruchów “w dół”
oraz “w prawo”. Wejście na dane pole kosztuje tyle, co znajdująca się tam liczba. Proszę podać algorytm
znajdujący trasę o minimalnym koszcie. """


def chess_path(A):
    n = len(A)
    dp = [[0 for _ in range(n)] for __ in range(n)]

    dp[0][0] = 0
    for i in range(1,n):
        dp[0][i] = dp[0][i-1] + A[0][i]
        dp[i][0] = dp[i-1][0] + A[i][0]

    for i in range(1,n):
        for j in range(1,n):
            better = min(dp[i-1][j],dp[i][j-1])
            dp[i][j] = better+A[i][j]

    for el in dp:
        print(el)
    return dp[n-1][n-1],dp

def get_solution(dp,i,j):
    if i == 0:
        res = []
        while j >= 0:
            res.append((i,j))
            j -= 1
        res.reverse()
        return res

    if j-1 < 0 or dp[i-1][j] < dp[i][j-1]:
        return get_solution(dp,i-1,j) + [(i,j)]
    return get_solution(dp,i,j-1) + [(i,j)]

A = [[5,1,-1,1],
     [-2,1,-3,4],
     [-2,7,1,6],
     [4,-3,1,3]]

n = len(A)
mincost,dp = chess_path(A)
print(get_solution(dp,n-1,n-1))
print(mincost)