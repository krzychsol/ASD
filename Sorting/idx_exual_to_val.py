"""
    Dana jest posortowana rosnąco tablica A wielkości n zawierająca parami różne liczby naturalne.
    Podaj algorytm, który sprawdzi, czy jest taki indeks i, że A[i] == i.
    Co zmieni się, jeżeli liczby będą po prostu całkowite, niekoniecznie naturalne?
"""


def binarySearch(A):
    p = 0
    r = len(A) - 1
    while p <= r:
        mid = (r - p) // 2
        if A[mid] == mid:
            return True
        elif A[mid] > mid:
            r = mid - 1
        else:
            p = mid + 1
    return False

A = [-6,-5,-3,-2,1,5,8,9]
print(binarySearch(A))