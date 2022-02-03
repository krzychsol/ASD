from random import randint

#ZAKŁADAM ŻE KOPIEC JEST JUZ DANY W ZADANIU ZATEM NIE LICZE CZASU
#NA TWORZENIE KOPCA MIN
'''
k razy usuwam najmniejszy element z kopca min (czyli wierzcholek)
na koncu sprawdzam czy nowy wierzcholek jest >= x
Zlożoność czasowa: O(klogn)
k razy wykonuje operacje usuniecia wierzcholka i naprawienia struktury kopca
kazde usuniecie i naprawienie jest w czasie O(logn),n - rozmiar kopca
'''

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapifymin(A,n,i):
    l = left(i)
    r = right(i)
    m = i

    if l<n and A[l] < A[m]:m=l
    if r<n and A[r] < A[m]:m=r
    if m != i:
        #swap
        A[i],A[m] = A[m],A[i]
        heapifymin(A,n,m)

def buildheap(A):
    n = len(A)
    for i in range(parent(n-1),-1,-1):
        heapifymin(A,n,i)

def deletetop(T):
    n = len(T)
    T[0],T[n-1] = T[n-1],T[0]
    T.pop()
    heapifymin(T,n-1,0)

def checkkthel(T,k,x):
    while k > 0:
        deletetop(T)
        k -= 1
    if T[0] >= x:
        return True
    return False

n = 10
T = [randint(1,15) for _ in range(n)]
print(T)
buildheap(T)
print(T)
print(checkkthel(T,3,4))