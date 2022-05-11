from zad7ktesty import runtests 

"""
Zadanie 7 - Oszczędny ogrodnik
Szablon rozwiązania: zad7k.py
W sadzie pewnego oszczędnego ogrodnika rosły drzewa owocowe. Jednak ze względu na 
brak wystarczającej ilości funduszy, nie ma on możliwości podlania wszystkich z nich. Musi 
wybrać, które drzewa podlać, aby ze sprzedaży owoców z nich zebranych osiągnąć jak 
największy przychód. (Aby podlać dane drzewo musimy podlać cały jego korzeń, tj. 
wszystkie jego fragmenty posiadające przynajmniej jeden wspólny bok). Dana jest tablica 
dwuwymiarowa T o wymiarach NxM która zawiera informacje o tym, czy na danej 
"współrzędnej" znajduje się korzeń jakiegoś drzewa i jeżeli tak, to ile litrów wody wymaga, 
aby został poprawnie podlany. Pierwsza współrzędna tablicy T określa głębokość, a druga 
lokalizację. Ze względów logistycznych ogrodnik posiada księgę, w której zapisane są 
lokalizacje wszystkich drzew w sadzie. Wyrażona jest poprzez tablicę liczb naturalnych D. 
Przykładowo, jeżeli D[i] = x, oznacza to, że w punkcie T[0][x] będzie znajdował się fragment 
korzenia drzewa i-tego. Można założyć, że na głębokości "zerowej" każde drzewo posiada 
tylko jeden fragment korzenia, oraz, że żadne dwa drzewa nie mają wspólnego korzenia. 
Księgowa ogrodnika przygotowała także zbiór (wyrażony tablicą liczb naturalnych Z) 
potencjalnych przychodów, które może osiągnąć ze zbiórki owoców (Tak, że dla drzewa w 
lokalizacji D[i], potencjalny przychód wynosi Z[i]). Proszę napisać algorytm, który zwróci 
maksymalny przychód, który ogrodnik może osiągnąć ze zbiorów, zakładając, że posiada on 
tylko l litrów wody, aby podlać swój ogród.
Algorytm należy zaimplementować jako funkcję postaci:
def ogrodnik( T, D, Z, l ):
 … 
która przyjmuje tablicę dwuwymiarową współrzędnych T, tablicę lokalizacji drzew D, tablicę 
potencjalnych zysków Z oraz limit litrów wody l.
Przykład. Dla danych:
D = [4, 9, 12, 16]
Z = [13, 11, 15, 4]
l = 32

Wynikiem jest liczba 28
"""

def linearize(T):
    n = len(T[0])
    m = len(T)

    def collect(j, i=0):
        nonlocal T, water, n, m

        if T[i][j] > 0:
            water += T[i][j]
            T[i][j] = 0
        else:
            return

        if i - 1 >= 0 and T[i - 1][j] > 0:
            collect(j, i - 1)
        if i + 1 < m and T[i + 1][j] > 0:
            collect(j, i + 1)
        if j + 1 < n and T[i][j + 1] > 0:
            collect(j + 1, i)
        if j - 1 >= 0 and T[i][j - 1] > 0:
            collect(j - 1, i)

    new = [0 for _ in range(n)]
    for i in range(n):
        water = 0
        collect(i)
        new[i] = water

    return new

def knapsack(W, P, maxW):
    n = len(W)

    # Tworze macierz programowania dynamicznego dla mojej funkcji f(i,j)
    F = [[0 for _ in range(maxW + 1)] for __ in range(n)]

    # Jeżeli biorę przedmiot nr.1 to wypełniam profity od momentu gdy mogę go
    # zabrać do plecaka
    for kol in range(W[0], maxW + 1):
        F[0][kol] = P[0]

    for i in range(1, n):
        for j in range(1, maxW + 1):
            F[i][j] = F[i - 1][j]  # wartość gdybyśmy nie brali przedmiotu
            if j >= W[i]:
                # bierzemy maxa z wartosci gdy wezmiemy i gdy nie wezmiemy
                F[i][j] = max(F[i][j], F[i - 1][j - W[i]] + P[i])

    return F[n - 1][maxW], F


def getsolution(F, W, P, i, w):
    if i == 0:
        if w >= W[i]:
            return [0]
        return []

    if w >= W[i] and F[i][w] == F[i - 1][w - W[i]] + P[i]:
        return getsolution(F, W, P, i - 1, w - W[i]) + [i]
    return getsolution(F, W, P, i - 1, w)


def ogrodnik (T, D, Z, l):
    T = linearize(T)
    k = len(D)
    for i in range(k):
        D[i] = T[D[i]]

    maxProfit,F = knapsack(D,Z,l)
    return maxProfit

runtests( ogrodnik, all_tests=True )
