"""
    Zaimplementuj funkcję average_score(arr, n, lowest, highest).
    Funkcja ta przyjmuje na wejściu tablicę n liczb rzeczywistych (ich
    rozkład nie jest znany, ale wszystkie są parami różne) i zwraca
    średnią wartość podanych liczb po odrzuceniu lowest najmniejszych
    oraz highest największych. Zaimplementowana funkcja powinna być
    możliwie jak najszybsza. Oszacuj jej złożoność czasową (oraz bardzo
    krótko uzasadnić to oszacowanie).
"""
"""
    Alogrytm: Wykonuje 2 razy algorytm magicznych piątek znajdując brzegowe elementy.
    Potem liniowo zliczam wynik i obliczam średnią.
    Złożoność obliczeniowa: O(n)
    Złożoność pamięciowa: 
"""
from math import ceil


### MEDIANA MEDIAN  ###

# Zwraca indeks mediany z posortowanej tablicy
def getmedian(p, r):
    return (r - p) // 2 + p


# Sortuje <=5 elementowe podtablice
def insertsort(A, p, r):
    for i in range(p, r + 1):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key


# Przyjmuje mediane median jako pivot i dzieli na elementy mniejsze,rowne,wieksze od niego.
def partition(A, p, r, k):
    i = p
    j = p
    while j < r:
        if A[j] < k:
            A[j], A[i] = A[i], A[j]
            i += 1
        elif A[j] == k:
            A[r], A[j] = A[j], A[r]
            j -= 1
        j += 1
    A[i], A[r] = A[r], A[i]
    return i


# Zwraca indeks mediany z nieposortowanej tablicy
def median5(A, p, r):
    for i in range(p, r + 1):
        cnt = p
        for j in range(p, r + 1):
            if A[i] > A[j]:
                cnt += 1
        if cnt == getmedian(p, r):
            return i


# Oblicza mediane median oraz wykorzystuje ją do znalezienia k-tego elementu, przy użyciu
# zmodyfikowanego quick selecta
def select(A, k, p, r):
    if p == r:
        return A[p]

    n = r - p + 1
    if n <= 5:
        insertsort(A, p, r)
        for i in range(p, r + 1):
            if i == k:
                return A[i]

    i = p
    while i < ceil(n / 5):
        x = median5(A, 5 * i, min(5 * i + 4, r))
        A[i], A[x] = A[x], A[i]
        i += 1

    y = select(A, getmedian(p, ceil(n / 5) + p), p, ceil(n / 5) - 1 + p)
    q = partition(A, p, r, y)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, k, p, q - 1)
    else:
        return select(A, k, q + 1, r)


# zwraca obliczony k-ty element tablicy
def linearselect(A, k):
    return select(A, k, 0, len(A) - 1)


### MAIN CODE ###
def average_score(arr, n, lowest, highest):
    lowElement = linearselect(arr, lowest)
    highElement = linearselect(arr, n - highest - 1)

    score = 0
    for i in range(n):
        if lowElement <= arr[i] <= highElement:
            score += arr[i]

    avg = score / (n - lowest - highest)
    return avg


A = [10, 5, 6, 2, 3, 7, 8, 9, 4, 1]
print(average_score(A, 10, 3, 3))
