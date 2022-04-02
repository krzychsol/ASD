"""
Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm
znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm powinien działać w czasie
wielomianowym względem liczby przedmiotów oraz sumy ich profitów
"""
"""
Funkcja f(i,j) = f(i-1,j) ,gdy i-ty przedmiot nie zmieści się w plecaku 
lub f(i,j) = max(f(i-1,j),f(i-1,j-W[i])+P[i]) ,gdzie W[i] to waga i-tego przedmiotu
a P[i] to wartość i-tego przedmiotu.

Innymi słowy gdy przedmiot i-ty zmieści się w plecaku bierzemy maksimum wartości
z przypadku gdybyśmy i-tego przedmiotu nie wzieli oraz gdybyśmy go wzięli.
"""
"""
Złożoność obliczeniowa: O(n*maxW)
Złożoność pamięciowa: O(n*maxW)
"""


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


W = [2, 1, 4, 4]  # lista wag
P = [4, 3, 6, 8]  # lista profitów
maxW = 8  # maksymalny ciężar jaki uniesiemy

maxP, F = knapsack(W, P, maxW)
print(maxP)
print(getsolution(F, W, P, len(W) - 1, maxW - 1))
