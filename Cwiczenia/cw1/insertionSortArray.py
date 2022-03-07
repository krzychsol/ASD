def insertion_sort( A ):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            A[j] = key
            j -= 1
    return A

A = [2,3,7,4,1]
print(insertion_sort(A))