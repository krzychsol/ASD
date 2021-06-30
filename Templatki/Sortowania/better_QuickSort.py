def quicksort(A,p,r):
    while p < r:
        q = partitionlomuto(A,p,r)
        if q-p < r-q:
            quicksort(A,p,q-1)
            p = q + 1
        else:
            quicksort(A,q+1,r)
            r = q - 1

def partitionlomuto(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p,r):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1