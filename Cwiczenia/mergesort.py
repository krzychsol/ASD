def merge(A,B):
    nA = len(A)
    nB = len(B)
    X = [None for _ in range(nA+nB)]

    idxA = 0
    idxB = 0
    while idxA < nA and idxB < nB:
        if A[idxA] <= B[idxB]:
            X[idxA+idxB] = A[idxA]
            idxA += 1
        else:
            X[idxA+idxB] = B[idxB]
            idxB += 1

    while idxA < nA:
        X[idxA+idxB] = A[idxA]
        idxA += 1

    while idxB < nB:
        X[idxA+idxB] = B[idxB]
        idxB += 1

    return X

def mergesort(A):
    n = len(A)
    if n <= 1:
        return A

    mid = n//2
    L = mergesort(A[:mid])
    R = mergesort(A[mid:])
    A = merge(L,R)

    return A

A = [9,3,7,1,4,2,5,3,6,8,3]
print(mergesort(A))