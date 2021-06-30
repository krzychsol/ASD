from random import randint, seed
from time import time

def countSort(A):
    n = len(A)
    R = [0 for _ in range(n)]

    #initialize count array
    C = [0 for _ in range(10)] #max A +1

    #store the count of each element in count array
    for i in range(n):
        C[A[i]] += 1

    #store the cummulative count
    for i in range(1,10):
        C[i] += C[i-1]

    #Find the index of each element of the original array in count array
    #place the elements in output array
    i = len(A)-1
    while i>=0:
        R[C[A[i]]-1] = A[i]
        C[A[i]] -= 1
        i -= 1

    #Copy the sorted elements into original array
    for i in range(n):
        A[i] = R[i]

seed(42)

T = [randint(1,9) for i in range(1000000)]

t1 = time()
countSort(T)
t2 = time()

for i in range(len(T) - 1):
    if T[i] > T[i + 1]:
        print("Błąd sortowania!")
        exit()

print("OK","Czas: ",t2-t1)
