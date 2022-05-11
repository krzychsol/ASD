from zad5ktesty import runtests

"""
Zadanie 5 - Ograj Garka
Szablon rozwiązania: zad5k.py
Dana jest talia N kart wyrażona poprzez tablicę A liczb naturalnych zawierającą wartości tych 
kart. Można przyjąć, że talia posiada parzystą ilość kart. Karty zostały rozłożone na bardzo 
szerokim stole w kolejności pojawiania się w tablicy. Dziekan poinformował Cię, że 
podwyższy Ci ocenę z WDI o pół stopnia, jeżeli wygrasz z nim w pewną grę, polegającą na 
braniu kart z jednego lub drugiego końca stołu na zmianę. Zakładając, że zaczynasz 
rozgrywkę, musisz znaleźć jaką maksymalnie sumę wartości kart uda Ci się uzyskać. 
Jednak, co ważne, musisz przyjąć, że dziekan jest osobą bardzo inteligentną i także będzie 
grał w 100% na tyle optymalnie, na tyle to możliwe. Aby nie oddawać losu w ręce szczęścia 
postanowiłeś, że napiszesz program, który zagwarantuje Ci wygraną (lub remis). Twój 
algorytm powinien powiedzieć Ci, jaka jest maksymalna suma wartości kart, którą masz 
szansę zdobyć grając z Garkiem.
Algorytm należy zaimplementować jako funkcję postaci:
def garek( A ):
 … 
która przyjmuje tablicę liczb naturalnych T i zwraca liczbę będącą maksymalną możliwą do 
uzyskania sumą wartości kart.
Przykład. Dla tablicy:
T = [8, 15, 3, 7]
Wynikiem jest liczba 22
"""

def garek ( A ):
    n = len(A)
    F = [[(0,0) for _ in range(n)] for __ in range(n)]

    for i in range(n):
        F[i][i] = (A[i],0)

    for i in range(n-1):
        F[i][i+1] = (max(A[i],A[i+1]),min(A[i],A[i+1]))

    for i in range(n-3,-1,-1):
        for j in range(i+2,n):
            if A[i]+F[i+1][j][1] > A[j]+F[i][j-1][1]:
                F[i][j] = (A[i]+F[i+1][j][1], F[i+1][j][0])
            else:
                F[i][j] = (A[j]+F[i][j-1][1],F[i][j-1][0])

    return F[0][n-1][0]

#T = [8,15,3,7]
#print(garek(T))
runtests ( garek )