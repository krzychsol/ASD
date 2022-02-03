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

from math import log

def insertionSort(T):
    n = len(T)
    for i in range(1,n):
        key = T[i]
        j = i-1
        while j>=0 and T[j] > key:
            T[j+1] = T[j]
            j -= 1
        T[j+1] = key
    return T

def bucketSort(T):
    n = len(T)
    norm = max(T)-min(T)
    B = [[] for _ in range(n)]

    for el in T:
        norm_el = (el-min(T))/norm
        idx = int(norm_el*n)
        if idx != n:
            B[idx].append(el)
        else:
            B[idx-1].append(el)

    for i in range(n):
        B[i] = insertionSort(B[i])

    idx = 0
    for i in range(n):
        for j in range(len(B[i])):
            T[idx] = B[i][j]
            idx += 1
    return T

def fast_sort(tab,a):
    n = len(tab)
    for i in range(n):
        tab[i] = log(tab[i],a)

    tab = bucketSort(tab)
    for i in range(n):
        tab[i] = a**tab[i]
    return tab

tab = [3.23,1.23,6.76,4.23,8.12]
print(fast_sort(tab,2))