'''
Mamy daną tablicę A z n liczbami naturalnymi.
Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
czy w tablicy ponad połowa elementów ma jednakową wartość.
'''

from random import randint

def bucketSort(T):
    n = len(T) #dlugosc tablicy
    norm = max(T)-min(T) #zmienna do normalizacji zakresu
    B = [[] for _ in range(n)] #tworze n kubelkow
    largest = 0 #max wielosc kubleka

    for el in T:
        norm_el = (el-min(T))/norm #normalizuje el do [0,1)
        bidx = int(norm_el*n) #wsadzam do odp kubleka
        if bidx != n:
            B[bidx].append(el)
            if len(B[bidx])>largest:
                largest = bidx
        else:
            B[bidx-1].append(el)
            if len(B[bidx-1])>largest:
                largest = bidx-1

    if largest>n/2:
        return True
    return False

# Driver Code
n = 30
x = [randint(1,1000000) for i in range(n)]
print(bucketSort(x))
