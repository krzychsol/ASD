from EGZAMIN20.Termin1.zad2testy import runtests
from math import inf

# f(i,j)= minimalny mozliwy do uzyskania wynik tymaczasowy w tablicy od i do j.
# f(i,j) = max( min(max(f(i,k),f(k+1,j))po k należacym od i do j) ,suma(i,j) )
def opt_sum(tab):
    n = len(tab)
    T = [0 for _ in range(n)]
    T[0] = tab[0]
    for i in range(1, n):
        T[i] = tab[i] + T[i - 1]

    # Sumy prefiksowe
    def suma(tab, T, i, j):
        if i == j:
            return tab[i]
        if i == 0:
            return T[j]
        return T[j] - T[i - 1]

    f = [[inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        f[i][i] = 0
    for i in range(n - 1):
        f[i][i + 1] = abs(tab[i] + tab[i + 1])

    # dlugosc - rozpatruje przedzialy kolejno 2,3,4,5,... elementowe
    for dlugosc in range(2, n):
        # nasze i zmienia się od 0 do n - długość, tutaj przedział zjebany wiec +1
        for i in range(0, n - dlugosc + 1):
            # j to i + długość przedziału
            j = i + dlugosc
            if j >= n:
                continue
            # mamy więc przedział w tablicy od i do j włącznie o długości dlugosc.
            # nasze k zmienia się od [i+1,...,j-1] jest to wstawienie nawiasowania do naszego dodawnia nadając mu kolejność
            for k in range(i, j):
                f[i][j] = min(f[i][j], max(f[i][k], f[k + 1][j], abs(suma(tab, T, i, j))))
    return f[0][n - 1]

    

opt_sum([1,-5,2])
runtests( opt_sum )
