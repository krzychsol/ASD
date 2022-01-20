from random import randint

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
    for i in range(n):
        A[i] = R[i]

def radixSort(T):
    max1 = max(T)
    exp = 1
    while max1/exp>0:
        countSort(T,exp)
        exp *= 10

T = [randint(160,220) for _ in range(15)]
print(T)
print()
radixSort(T)
print(T)