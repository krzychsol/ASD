'''
Algorytm najpierw oblicza dlugosc najdluzszego podciagu rosnacego ,tablice przechowujaca dlugosc najdluzszych podciagow rosnacych konczacych sie na indeksie i-tym (tyle ze tablica jest odwrocona)
oraz tablice pozwalajaca odtworzyc te podciagi. Te informacje sa wykorzystywane w funkcji rekurencyjnej getsolution, która odtwarza wyniki i przy okazji oblicza ich ilość.
Złożoność czasowa funkcji LIS : O(n^2)
Złożoność czasowa całego algorytmu licząć z wypisywaniem wyników : 0(2^n)
'''

def LIS( A ):
    n = len(A)
    #tablica dlugosci maksymalnych podciagow malejacych konczacych sie na i-tym indeksie
    F = [1] * n
    #tablica 'mapa' sluzaca do odtworzenia wynikowych podciągów ,zawiera ona indeksy
    C = [[[None] * n, -1, -1] for _ in range(n)]

    #w petlach szukam najdluzszych podciagow malejacych zaczynajac od konca tablicy
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if A[j] > A[i] and F[j] + 1 >= F[i]:
                if F[j] + 1 > F[i]:
                    F[i] = F[j] + 1
                    #przesuwamy sie w tablicy poniewaz znalezlismy dluzszy podciag
                    C[i][1] = C[i][2] = C[i][2] + 1

                #tworzy sie nam nowe rozgalezienie
                C[i][0][C[i][2]] = j
                C[i][2] += 1

    return max(F), F, C

def printAllLIS( A ):
    cnt = 0
    def getsolution(A, C, res, idx, i):
        nonlocal cnt
        if idx == 1: #gdy zostal ostatni element podciagu ,to mozemy go wypisac
            res[len(res) - idx] = A[i]
            for i in range(len(res)):
                print(res[i], end=" ")
            print()
            #zwiekszamy licznik
            cnt += 1
            return

        res[len(res) - idx] = A[i]
        for j in range(C[i][1], C[i][2]):
            #wywolujemy rekurencje dla rozgalezien
            getsolution(A, C, res, idx - 1, C[i][0][j])

    maxlen, F, C = LIS(A)
    #w tablicy res bedziemy zapisywali odtworzony podciag
    res = [-1] * maxlen
    #w petli odtwarzamy wszystkie podciagi o maksymalnej dlugosci
    for idx in range(len(A)):
        if F[idx] == maxlen:
            getsolution(A, C, res, maxlen, idx)

    return cnt
