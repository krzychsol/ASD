# Jeżeli nie dokonamy żadnego swapa to przerywamy algorytm bo to oznacza że
# Tablica juz jest posortowana
# Czas pesymistyczny O(n^2)
# Czas optymistyczny O(n)

import time
from random import seed, randint


def bubble_sort(T):
    n = len(T)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if T[j] > T[j + 1]:
                T[j], T[j + 1] = T[j + 1], T[j]
                swapped = True

        if not swapped:
            break

    return T

#Generowanie losowej tablicy
seed(1)
n = 10000
A = [0 for _ in range(n)]
for i in range(n):
    A[i] = randint(0,10000)

#Liczenie czasu
start = time.time()
bubble_sort(A)
end = time.time()
print("Czas: ", end - start)
