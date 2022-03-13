import time
from random import seed, randint

def select_sort( T ):
    n = len(T)
    for i in range(n):
        idx = i
        for j in range(i+1,n):
            if T[idx] > T[j]:
                idx = j
        T[idx],T[i] = T[i],T[idx]
    return T


# Generowanie losowej tablicy
seed(1)
n = 20000
A = [0 for _ in range(n)]
for i in range(n):
    A[i] = randint(0,10000)

# Liczenie czasu
start = time.time()
select_sort(A)
end = time.time()
print("Czas: ", end - start)

