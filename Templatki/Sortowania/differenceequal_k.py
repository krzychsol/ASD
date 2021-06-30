def bin_search(A,low,high,x):
    while low <= high:
        mid = (low+high)//2
        if x == A[mid]:
            return mid
        if A[mid] < x:
            low = mid+1
        else:
            high = mid
    return -1

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

def countPairswithdiffK(A,k):
    n = len(A)
    cnt = 0
    quicksort(A,0,n-1)
    for i in range(len(A)-1,0,-1):
        if A[i] == A[i-1]:
            del A[i]

    n = len(A)
    for i in range(n-1):
        if bin_search(A,i+1,n-1,A[i]+k) != -1:
            cnt += 1
    return cnt

T = [1,5,3,4,2,2,4,5,3]
k = 3
print(countPairswithdiffK(T,k))