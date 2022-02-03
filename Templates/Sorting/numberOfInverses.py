from random import randint

def merge(A,aux,low,mid,high):
    k = i = low
    j = mid+1
    invcnt = 0

    while i<=mid and j<=high:
        if A[i] <= A[j]:
            aux[k] = A[i]
            i += 1
        else:
            aux[k] = A[j]
            j += 1
            invcnt += (mid-i+1)
        k += 1

    while i <= mid:
        aux[k] = A[i]
        k += 1
        i += 1

    for i in range(low,high+1):
        A[i] = aux[i]

    return invcnt

def mergesort(A,aux,low,high):
    if low == high:
        return 0

    mid = (low+high)//2
    invcnt =  0

    invcnt += mergesort(A,aux,low,mid)
    invcnt += mergesort(A,aux,mid+1,high)
    invcnt += merge(A,aux,low,mid,high)

    return invcnt

#DRIVER CODE

if __name__ == '__main__':
    A = [1,9,6,4,5]
    aux = A.copy()
    print("Inwersji: ",mergesort(A,aux,0,len(A)-1))




