'''
Dana jest macierz o rozmiarze MxN, zawierająca komórki bezpieczne (o wartości 0 lub 1)
oraz niebezpieczne (-1). Należy znaleźć ścieżkę o największej liczbie "1", zaczynając
z komórki matrix[0][0]; możemy poruszać się tylko po komórkach bezpiecznych oraz
w wierszach parzystych możemy iść tylko w dół lub w prawo, natomiast w nieparzystych
- w dół lub w lewo.
'''


# ALGORYTM:
'''
Tworzymy macierz pomocniczą dp o wymiarach takich jak wejściowa. W dp[i][j] znajduje się
wartość najlepszej ścieżki kończącej się w komórce matrix[i][j]. Wypełniamy tę macierz
kolejno wierszami. Jeżeli matrix[i][j] ma wartość -1, to wiemy na pewno, że dp[i][j] == 0.
Jeżeli jesteśmy w wierszu parzystym i matrix[i][j] != -1, to bierzemy wartość 
max(dp[i][j-1], dp[i-1][j]) + matrix[i][j], bo mogliśmy przyjść z góry lub z lewej,
analogicznie dla wierszy nieparzystych. Uważamy również na to, by nie wyjść poza  macierz.
'''

def inside(i,j,lenght,height): #czy nie wychodze za tablice
    return (0 <= i < height) and (0 <= j < lenght)

def best_path(M):
    m = len(M[0])
    n = len(M)
    best = 0
    dp = [[0 for _ in range(m)]for __ in range(n)]

    for i in range(n):
        if i % 2 == 0:
            for j in range(m): #od lewej do prawej
                if M[i][j] == -1:
                    dp[i][j] = 0
                elif i == 0 and j == 0:
                    dp[i][j] = M[i][j]
                else:
                    fromUp = 0
                    fromLeft = 0
                    if inside(i-1,j,m,n):
                        fromUp = dp[i-1][j]
                    if inside(i,j-1,m,n):
                        fromLeft = dp[i][j-1]
                    dp[i][j] = max(fromUp,fromLeft)+M[i][j]
                    if dp[i][j] > best:
                        best = dp[i][j]

        else:
            for j in range(m-1,-1,-1): #od prawej do lewej
                if M[i][j] == -1:
                    dp[i][j] = 0
                else:
                    fromUp = 0
                    fromRight = 0
                    if inside(i - 1, j, m, n):
                        fromUp = dp[i - 1][j]
                    if inside(i, j + 1, m, n):
                        fromRight = dp[i][j + 1]
                    dp[i][j] = max(fromUp, fromRight) + M[i][j]
                    if dp[i][j] > best:
                        best = dp[i][j]

    return best

M = [
        [1,1,1,1,1],
        [1,0,1,0,1],
        [-1,-1,-1,-1,-1],
        [1,1,1,1,1],
        [0,0,0,0,0]
    ]

print(best_path(M))