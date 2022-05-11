"""
Dana jest dwuwymiarowa tablica T o rozmiarach N × N wypełniona liczbami naturalnymi (liczby
są parami różne). Proszę zaimplementować funkcję Median(T), która przekształca tablicę T, tak
aby elementy leżące pod główną przekątną nie były większe od elementów na głównej przekątnej,
a elementy leżące nad główną przekątną nie były mniejsze od elementów na głównej przekątnej.
Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci ponad tę, która potrzebna
jest na przechowywanie danych wejściowych (choć algorytm nie musi działać w miejscu). Proszę
podać złożoność czasową i pamięciową zaproponowanego algorytmu.
"""


def partition(t, p, k):
    pivot = t[k]
    last = p-1
    for i in range(p, k):
        if t[i] <= pivot:
            last += 1
            t[last], t[i] = t[i], t[last]
    t[last+1], t[k] = t[k], t[last+1]
    return last+1


def select(t, k, p=0, r=None):
    if r is None: r = len(t)-1

    q = partition(t, p, r)
    if k < q:
        return select(t, k, p, q-1)
    elif k == q:
        return t[q]
    else:
        return select(t, k, q+1, r)


def linearize(tab):
    n = len(tab)
    output = []
    for i in range(n):
        output.extend(tab[i])
    return output


def MedianT(T):
    n = len(T)
    L = linearize(T)
    print(L)
    for i in range(n):
        T[i][i] = select(L,int((n/2)*(n-1))+i)


    idx = 0
    for i in range(1,n):
        for j in range(i):
            T[i][j] = L[idx]
            idx += 1

    idx += n
    for i in range(n):
        for j in range(i+1,n):
            T[i][j] = L[idx]
            idx += 1

    return T

T4 = [ [43, 74, 53, 97], [80, 61, 61, 19], [61, 73, 89, 93], [42, 17, 89, 80] ]
R = MedianT(T4)
for el in R:
    print(el,end=" ")