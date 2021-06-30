def bubbleSort(A):
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            if A[i]>A[j]:
                A[i],A[j] = A[j],A[i]

A = [3,1,5,3,4,7,9,11,1,4,2]
bubbleSort(A)
print(A)