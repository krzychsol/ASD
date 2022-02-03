###ĆWICZENIA Z ASD: ZASTOSOWANIA SORTOWAŃ###
"""
Dana jest posortowana tablica int A[N] oraz liczba x. Napisać program, który stwierdza czy istnieją
indeksy i oraz j, takie że A[i] + A[j] = x (powinno działać w czasie O(N)).
"""

def isSumExist(A,x):
    n = len(A)
    i = 0
    j = n-1
    while i != j:
        if A[i]+A[j] == x:
            return True
        elif A[i]+A[j] < x:
            i += 1
        else:
            j -= 1

    return False

A = [2,3,5,7,11,13,17,19,23]
print(isSumExist(A,41))