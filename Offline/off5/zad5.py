#from zad5testy import runtests
from Offline.off5.zad5testy import runtests
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

def plan(T):
    n = len(T)
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

runtests( plan, all_tests = True)