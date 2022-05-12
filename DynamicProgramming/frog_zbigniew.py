"""
Żab Zbigniew skacze po osi liczbowej. Ma się dostać z zera do n − 1, skacząc wyłącznie w kierunku
większych liczb. Skok z liczby i do liczby j (j > i) kosztuje Zbigniewa j − i jednostek energii, a jego
energia nigdy nie może spaść poniżej zera. Na początku Zbigniew ma 0 jednostek energii, ale na
szczęście na niektórych liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
(wartość przekąki dodaje się do aktualnej energii Zbigniewa).
Proszę zaimplementować funkcję zbigniew(A), która otrzymuje na wejściu tablicę A długości
len(A) = n, gdzie każde pole zawiera wartość energetyczną przekąski leżącej na odpowiedniej liczbie.
Funkcja powinna zwrócić minimalną liczbę skoków potrzebną, żeby Zbigniew dotarł z zera do
n-1 lub −1 jeśli nie jest to możliwe.

Podpowiedź. Warto rozważyć funkcję f(i, y) zwracającą minimalną liczbę skoków potrzebną by
dotrzeć do liczby i mając w zapasie dokładnie y jednostek energii.
Przykład. Dla tablicy A = [2,2,1,0,0,0] wynikiem jest 3 (Zbigniew skacze z 0 na 1, z 1
na 2 i z 2 na 5, kończąc z zerową energią). Dla tablicy A = [4,5,2,4,1,2,1,0] wynikiem jest 2
(Zbigniew skacze z 0 na 3 i z 3 na 7, kończąc z jedną jednostką energii).
"""

def zbigniew(A):
    n = len(A)
    F = [[float("inf") for _ in range(n)]for __ in range(n)]

    for i in range(n):
        A[i] = min(A[i],n-1)

    for i in range(A[0]+1):
        F[0][i] = 0

    for i in range(1,n):
        for j in range(n):
            for k in range(i):
                y = i-k+j-A[i]
                if 0 <= y < n:
                    F[i][j] = min(F[i][j],F[k][y]+1)

    return min(F[n-1])


print(zbigniew([4,5,2,4,1,2,1,0]))