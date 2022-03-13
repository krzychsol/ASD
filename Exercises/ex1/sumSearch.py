"""
Dana jest posortowana tablica A.
Szukamy zadanej sumy x takiej, że A[i]+A[j] = x
"""


def sum_search(T, x):
    n = len(T)
    p = 0
    q = n - 1
    while p < q:
        if T[p] + T[q] == x:
            return True
        elif T[p] + T[q] > x:
            q -= 1
        else:
            p += 1

    return False


A = [1, 5, 7, 9, 11, 16]
print(sum_search(A, 11))
