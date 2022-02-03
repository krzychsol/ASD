'''
Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu. Proszę zaimplementować funkcję:
section(T,p,q)
która zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie. Użyty algorytm
powinien być możliwie jak najszybszy. Proszę w rozwiązaniu umieścić 1-2 zdaniowy opis
algorytmu oraz proszę oszacować jego złożoność czasową.
'''

from random import randint
from math import pow

def countSort(A,exp):
    n = len(A)
    R = [0 for _ in range(n)]

    #initialize count array
    C = [0 for _ in range(10)] #max A +1

    #store the count of each element in count array
    for i in range(n):
        idx = (A[i] / exp)
        C[int(idx%10)] += 1

    #store the cummulative count
    for i in range(1,10):
        C[i] += C[i-1]

    #Find the index of each element of the original array in count array
    #place the elements in output array
    i = len(A)-1
    while i>=0:
        idx = (A[i]/exp)
        R[C[int(idx%10)]-1] = A[i]
        C[int(idx%10)] -= 1
        i -= 1

    #Copy the sorted elements into original array
    for i in range(len(A)):
        A[i] = R[i]

def radixSort(T):
    max1 = T[0]
    exp = 1
    while max1/exp>0:
        countSort(T,exp)
        exp *= 10

def printsoliders(T,p,q):
    for i in range(len(T)-1-p,len(T)-1-p-q,-1):
        print(T[i],end=" ")

n = 10
T = [randint(160,220) for _ in range(n)]
radixSort(T)
print(T)
printsoliders(T,1,4)