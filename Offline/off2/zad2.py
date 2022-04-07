# Krzysztof Solecki
"""
Opis algorytmu: Najpierw sortuje listę przedziałów rosnąco po początkach ,następnie dla jednakowych początków sortuje malejąco po końcach przedziałów.
Potem przechodzę po posrotowanej tablicy przedziałów i dopóki kolejne przedziały zawierają się w sobie zwiększam wysokość i aktualizuje jeśli jest większa od
największej dotychczas. Jeśli przedział sie nie zawiera w bieżącym rozpatrywanym oraz są one rozłączne to traktuje go jako nowy rozpatrywany przedział.

Złożoność obliczeniowa: Sortowanie - O(nlogn)
                        Szukanie maksymalnej wysokości - O(n^2) w przypadku pesymistycznym, O(n) w optymistycznym
                        Złożoność całego algorytmu to :
                            - pesymistyczna: O(n^2)
                            - optymistyczna: O(nlogn)
Złożoność pamięciowa: O(1)
"""
from Offline.off2.zad2testy import runtests


def partition(A, p, r):
    pivot = A[p][0]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while A[i][0] < pivot:
            i += 1

        j -= 1
        while A[j][0] > pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]


def quickSort(A, p, r):
    if p < r:
        pi = partition(A, p, r)
        quickSort(A, p, pi)
        quickSort(A, pi + 1, r)


def partitionDesc(A, p, r):
    pivot = A[p][1]
    i = p - 1
    j = r + 1

    while True:
        i += 1
        while A[i][1] > pivot:
            i += 1

        j -= 1
        while A[j][1] < pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]


def quickSortDesc(A, p, r):
    if p < r:
        pi = partitionDesc(A, p, r)
        quickSortDesc(A, p, pi)
        quickSortDesc(A, pi + 1, r)


def insertion_sort(A, p, r):
    for i in range(p + 1, r + 1):
        key = A[i][1]
        j = i - 1
        while j >= p and A[j][1] < key:
            A[j + 1][1] = A[j][1]
            A[j][1] = key
            j -= 1


def included(A, B):  # czy B zawiera się w A
    return B[0] >= A[0] and B[1] <= A[1]


def depth(L):
    n = len(L)
    quickSort(L, 0, n - 1)

    i = 0
    while i < n:
        start = i
        i = i + 1
        while i < n and L[i][0] == L[start][0]:
            i += 1
        if i - start <= 5:
            insertion_sort(L, start, i - 1)
        else:
            quickSortDesc(L, start, i - 1)

    maxHeight = 0
    height = 0
    curr = 0
    i = 1
    while i < n:
        while i < n and included(L[curr], L[i]):
            height += 1
            i += 1
        tmp = i
        while tmp < n and L[tmp][0] < L[curr][1]:
            if included(L[curr], L[tmp]):
                height += 1
            tmp += 1
        maxHeight = max(maxHeight, height)
        curr = i
        height = 0
        i += 1

    return maxHeight


runtests(depth)
