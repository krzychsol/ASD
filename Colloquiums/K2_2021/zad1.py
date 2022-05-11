# Krzysztof Solecki
"""
Opis algorytmu:
Algorytm opiera się na dynamicznie obliczanej funkcji F(i,j) - największa liczba studentów rozmieszczona w budynkach od 0 do i przy
maksymalnym koszcie budowy j (pamiętając ,że budynki nie mogą na siebie nachodzić).
Wzór funkcji: F[i][j] = max{F[i][j],F[k][j-w[i-1]+capacity(i-1)},gdzie:
    * k - indeks ostatniego budynku poprzedzającego i-ty budynek i nienachodzący na niego.
    * w[i] - koszt budowy i-tego budynku
    * capacity(i) - pojemność i-tego budynku

Po obliczeniu tablicy F jesteśmy w stanie odtworzyć listę użytych budynków ,pamiętając przy tym pod jakim indeksem w oryginalnej tablicy
znajdował się każdy z budynków (algorytm sortuje oryginalną tablicę po końcach przedziałów [a,b] budynków).

Złożoność czasowa: O(nlogn)+O(n*p)
Złożoność pamięciowa: O(n*p) ,gdzie n to ilość budynków w tablicy T ,p to maksymalny koszt budowy budynków.
"""

from zad1testy import runtests


# ilosc mieszkancow budynku
def cap(T, i):
    return T[i][0] * (T[i][2] - T[i][1])


# funkcja zwraca ostatni budynek nieprzecinajacy się z budynkiem i-tym
def last_not_intercept(T, i):
    i -= 1
    a = T[i][1]
    for j in range(i - 1, -1, -1):
        b = T[j][2]
        if b < a:
            return j + 1

    return 0


def select_buildings(T, p):
    def get_solution(F, i, j):
        if i == 0:
            return
        if F[i][j] == F[i - 1][j]:
            get_solution(F, i - 1, j)
            return

        prev = last_not_intercept(T, i)
        if F[i][j] == F[prev][j - T[i - 1][3]] + cap(T, i - 1):
            get_solution(F, prev, j - T[i - 1][3])
            buildings.append(T[i - 1][4])
            return

    n = len(T)
    for i in range(n):
        # pamiętam indeksy z oryginalej tablicy
        # potrzebne do odtworzenia wyniku w oryginalnej kolejności
        T[i] = [T[i][0], T[i][1], T[i][2], T[i][3], i]

    T.sort(key=lambda x: x[2])
    F = [[0 for _ in range(p)] for __ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(p):
            prev = last_not_intercept(T, i)
            F[i][j] = max(F[i][j], F[i - 1][j])
            if j - T[i - 1][3] >= 0:
                F[i][j] = max(F[i][j], F[prev][j - T[i - 1][3]] + cap(T, i - 1))

    i = p - 1
    while F[n][i] == F[n][p - 1]:
        i -= 1

    buildings = []
    get_solution(F, n, i + 1)
    buildings.sort()

    return buildings


runtests(select_buildings)

