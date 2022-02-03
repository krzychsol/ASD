from math import *

'''
Algorytm dynamiczny ktory najpierw oblicza dlugosc najkrotszej trasy (najkrotszego cyklu Hamiltona) oraz uzupelnia tablice potrzebna do odtworzenia wyniku.
Nastepnie rekurencyjnie odtwarza pierwszą część trasy, czyli tej połowy trasy przed zmianą kierunku z "w prawo" na "w lewo". Na końcu do wyniku dopisuje jeszcze
drugą połowę trasy czyli miasta nie wymienione w pierwszej połowie ,wystepujace w kolejnosci malejącej wzgledem wspolrzednej x miasta.
Złożoność obliczeniowa algorytmu : O(n^2)
'''

#funkcja obliczajaca dystans miedzy dwoma punktami
def dist(C,i,j):
    return sqrt((C[i][1] - C[j][1]) ** 2 + (C[i][2] - C[j][2]) ** 2)

#funkcja odtawrzajaca rekurencyjnie pierwsza polowe trasy
def get_path(path, i, j, n):
    if n < 0:
        return []
    if i <= j:
        k = path[i][j]
        return [k] + get_path(path, k, j, n - 1)
    else:
        k = path[j][i]
        return get_path(path, i, k, n - 1) + [k]

def bitonicTSP(C):
    #sortuje tablice po wartosciach wspolrzednych x-owych rosnąco
    n = len(C)
    C = sorted(C, key=lambda x: x[1])

    #tablica 2d służąca do dynamicznego sumowania dlugosci najlepszych tras miedzy miastami i,j
    maxval = float('inf')
    D = [[maxval for _ in range(n)]for _ in range(n)]

    #tablica 2d sluzaca do przechowywania punktow "poprzednikow" ,aby pozniej mozna bylo odtworzyc pierwsza czesc trasy
    path = [[-1 for _ in range(n)]for _ in range(n)]

    #Zapisuje dystans miedzy ostatnim i przedostatnim miastem
    D[0][1] = dist(C,0,1)

    #Zapisuje indeks ostatniego miasta pierwszej polowy trasy(tego ,po którym zmienia kierunek poruszania się na przeciwny)
    path[0][1] = 0

    # w petli wykonuje funkcje dynamiczna realizujacą funkcje:
    # f(i,j) = f(i,j-1)+dist(j-1,j) ,i < j-1
    # f(j-1,j) = min(f(k,j-1)+dist(k,j)) ,k < j-1
    # przy okazji zapisu w tablicy D danej odleglosci zapisuje tez w tablicy path indeks miasta "poprzednika"
    # domyslnie odleglosci miedzy miastami sa wypelnione bardzo dużą wartoscia sluzacą jako infinity
    '''for i in range(n - 3, -1, -1):
        m = maxval
        for k in range(i + 2, n):
            if m > D[i + 1][k] + dist(C, i, k):
                m, mk = D[i + 1][k] + dist(C, i, k), k
                D[i][i + 1] = m
                path[i][i + 1] = mk
        for j in range(i + 2, n):
            D[i][j] = D[i + 1][j] + dist(C, i, i + 1)
            path[i][j] = i + 1'''

    for j in range(1,n):
        for i in range(0,j-1):
            if i < j-1:
                D[i][j] = D[i][j-1] + dist(C,j-1,j)
                path[i][j] = j-1
            else:
                D[i][j] = maxval
                for k in range(i-1):
                    best = D[k][i] + dist(C,k,j)
                    if best < D[i][j]:
                        D[i][j] = best
                        path[i][j] = k

    S = [[],[]]
    k = 0
    i = n-2
    j = n-1
    while j > 0:
        S[k].append(j)
        j = path[i][j]
        if j < i:
            i,j = j,i
            k = 1-k

    S[0].append(0)
    print(S[0],S[1])
    while S[1]:
        S[0].append(S[1].pop())

    print(S[0])
    for i in range(len(S[0])-1,-1,-1):
        print(S[0][i],end=" ")

    print(D)

C = [["Wrocław", 0, 2], ["Warszawa",4,3],["Gdańsk", 2,4], ["Kraków",3,1]]
bitonicTSP(C)