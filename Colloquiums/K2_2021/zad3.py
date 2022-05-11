from zad3testy import runtests
from queue import PriorityQueue
"""
Opis algorytmu: 
    Algorytm opiera się na zachłannym podejściu : za każdym razem zbieramy największą plamę jaką mamy w zasięgu i sprawdzamy 
    czy możemy dojechać do mety. Zawsze możemy zbierać najwięszką plamę, ponieważ mamy nieograniczony bak, stąd to podejście 
    jest poprawne.

Złożoność obliczeniowa:
    O(nlogn) - przechodzimy po liście liniowo (każde pole odwiedzamy maksymalnie raz),plamy ropy zbieramy do kolejki priorytetowej,
                na której operacje wstawiania i wyciągania kosztują O(logn) czasu. Na końcu sortujemy w czasie O(nlogn) wynikową listę
                postojów.

Złożoność pamięciowa: O(n)
"""

def linearize(T):
    n = len(T[0])
    m = len(T)

    def collect(j, i=0):
        nonlocal T, ropa, n, m

        if T[i][j] > 0:
            ropa += T[i][j]
            T[i][j] = 0
        else:
            return

        if i - 1 >= 0 and T[i - 1][j] > 0:
            collect(j, i - 1)
        if i + 1 < m and T[i + 1][j] > 0:
            collect(j, i + 1)
        if j + 1 < n and T[i][j + 1] > 0:
            collect(j + 1, i)
        if j - 1 >= 0 and T[i][j - 1] > 0:
            collect(j - 1, i)

    new = [0 for _ in range(n)]
    for i in range(n):
        ropa = 0
        collect(i)
        new[i] = ropa

    return new

def plan(T):
    n = len(T)
    T = linearize(T)
    result = [0]
    last = 0
    fuel = T[0]
    T[0] = 0
    Q = PriorityQueue()

    while fuel < n-1:
        for i in range(last, fuel+1):
            if T[i]:
                Q.put((-T[i], -i)) #wrzucam do kolejki wszystkie plamy ropy w zasięgu

        biggest_station, idx = Q.get() #wyciagam najwieksza plame z kolejki
        biggest_station *= -1
        idx *= -1

        last = fuel+1
        fuel += biggest_station
        T[idx] = 0
        result.append(idx)

    result.sort()
    return result

runtests(plan)
