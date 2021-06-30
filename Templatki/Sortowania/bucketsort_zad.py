'''
Mamy dane n punktów (x, y) w okręgu o promieniu k (liczba naturalna),
tzn. 0 <= x2 + y2 <= k, które są w nim równomiernie rozłożone, tzn.
Prawdopodobieństwo znalezienia punktu na danym obszarze jest proporcjonalne do pola tego obszaru.
Napisz algorytm, który w czasie Θ(n) posortuje punkty po ich odległości do punktu (0, 0), tzn.
d = sqrt(x2 + y2).
'''

from random import randint
from math import sqrt

def d(x,y):
    return sqrt(x*x+y*y)

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and d(A[j][0],A[j][1]) > d(key[0],key[1]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def bucketSort(T,k):
    n = len(T) #dlugosc tablicy
    maxd = 0
    mind = 2*k
    for i in range(n):
        if d(T[i][0],T[i][1])>maxd:
            maxd = d(T[i][0],T[i][1])
        if d(T[i][0],T[i][1])<mind:
            mind = d(T[i][0],T[i][1])

    norm = maxd-mind #zmienna do normalizacji zakresu
    B = [[] for _ in range(n)] #tworze n kubelkow

    for i in range(n):
        norm_el = (d(T[i][0],T[i][1])-mind)/norm #normalizuje el do [0,1)
        bidx = int(norm_el*n) #wsadzam do odp kubleka
        if bidx != n:
            B[bidx].append(T[i])
        else:
            B[bidx-1].append(T[i])

    for i in range(n): #sortuje kubelki
        B[i] = insertionSort(B[i])

    idx = 0
    for i in range(n): #lacze kubelki i daje do wejsciowej tablicy
        for j in range(len(B[i])):
            T[idx] = B[i][j]
            idx+=1

    return T

# Driver Code
n = 30
k = 4
x = [(-1,0),(-2,1),(-3,2),(-1,1),(-1,2),(2,3),(-1,-3),(-2,3),(1,2),(-3,-3),(-2,-2)]
print(x)
print(bucketSort(x,k))
