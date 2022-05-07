from zad3testy import runtests
"""
Mamy danych n przedziałów domkniętych {[a0,b0],[a1,b1], ... , [an-1,bn-1]} oraz liczbę k.
Mamy wyznaczyć k przedziałów spośród podanych takich, że ich przecięcie jest największe.

Rozwiązanie: Zapamiętuje indeksy w oryginalnej tablicy. Sortuje rosnaco po koncach.
Dla każdego przedzialu idąc od początku dobieram k-1 przedziałów idąc od końca na bieżąco
licząc przecięcie. Gdy znajdę już k takich przedziałów to aktualizuję z najwiekszym mozliwym przecieciem.

O(n^2)
"""


def kintersect( A, k ):
    n = len(A)
    for i in range(n):
        A[i] = A[i][0],A[i][1],i

    A = sorted(A,key=lambda x:x[1])
    maxIntersect = -float("inf")
    result = []

    for i in range(n):
        start = A[i][0]
        end = A[i][1]
        temp_max = end-start
        cnt = 1
        resultTmp = [A[i][2]]
        for j in range(n-1,-1,-1):
            if cnt == k:
                break
            if i != j and A[j][0] <= start < A[j][1]:
                cnt += 1
                temp_max = min(end,A[j][1])-start
                resultTmp.append(A[j][2])

        if temp_max > maxIntersect and cnt == k:
            maxIntersect = temp_max
            result = resultTmp

    return result

runtests( kintersect )