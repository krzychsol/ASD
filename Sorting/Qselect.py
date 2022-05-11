from random import randrange

def partitionrand(A,p,r):
    x = randrange(p,r)
    i = p-1
    for j in range(p,r,1):
        if A[j] <= x:
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def kthsmallest(A,p,r,k):
    if k>0 and k <= r-p+1:
        q = partitionrand(A,p,r)

        if q-p == k-1:
            return A[q]

        if q - p > k-1:
            return kthsmallest(A,p,q-1,k)

        return kthsmallest(A,q+1,r,k-q+p-1)

A = [1,5,2,4,3]
print(kthsmallest(A,0,len(A)-1,3))