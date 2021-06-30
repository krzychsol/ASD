from EGZAMIN20.Termin1.zad3testy import runtests
import math

def insertion(T):
    for i in range(1, len(T)):
        temp = T[i]
        j = i - 1
        while (j >= 0 and temp < T[j]):
            T[j + 1] = T[j]
            j = j - 1
        T[j + 1] = temp

def bucket_sort(T):
    largest = max(T)
    length = len(T)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(T[i] / size)

        if j != length:
            buckets[j].append(T[i])
        else:
            buckets[length - 1].append(T[i])

    for i in range(length):
        insertion(buckets[i])

    res = []

    for i in range(length):
        res = res + buckets[i]

    return res

def fast_sort(tab, a):
    n = len(tab)
    for i in range(n):
        tab[i] = math.log(tab[i],a)

    tab = bucket_sort(tab)
    for i in range(n):
        tab[i] = a**tab[i]

    return tab

runtests( fast_sort )
