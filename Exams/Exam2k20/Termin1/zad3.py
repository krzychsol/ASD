"""
Pewien eksperyment fizyczny daje w wyniku liczby rzeczywiste postaci a**x
, gdzie a to pewna stała większa od 1 (a > 1) zaś x to liczby rzeczywiste rozłożone równomiernie na przedziale [0, 1].
Napisz funkcję fast sort, która przyjmuje tablicę liczb z wynikami eksperymentu oraz stałą a i
zwraca tablicę z wynikami eksperymentu posortowanymi rosnąco. Funkcja powinna działać możliwie jak najszybciej. Uzasadnij poprawność zaproponowanego rozwiązania i oszacuj jego złożoność
obliczeniową. Nagłówek funkcji fast sort powinien mieć postać:
def fast_sort(tab, a):

"""
"""
Moje rozwiązanie: Algorytm wykorzystuje sortowanie kubełkowe: Najpierw logarytmuje elementy tablicy aby uzyskać tablicę potęg,
które nastepnie sortuje sortowaniem kubełkowym (można tak zrobić ponieważ funkcja logarytmiczna o podstawie > 1 jest rosnąca oraz
różnowartościowa więc posortowanie wykładników ustawia pierwotne liczby w odpowiedniej kolejności). Na końcu przywracamy pierwotną tablicę 
zamieniając kazdy element i-ty tablicy na a**i.

Złożność algroytmu : O(n) 
"""

from .zad3testy import runtests
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
