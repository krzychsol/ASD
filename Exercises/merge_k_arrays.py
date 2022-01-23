### ĆWICZENIA Z ASD : SORTOWANIA,MERGESORT ###  NIEZROBIONE !!!!#
"""
Proszę zaproponować/zaimplementować algorytm scalający k posortowanych tablic o łącznej długości n
w jedną posortowaną tablicę w czasie O(n ∗ log(k))
"""

def merge(L,R):
    res = [None for x in range(len(L)+len(R))]
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res[i+j] = L[i]
            i += 1
        else:
            res[i+j] = R[j]
            j += 1

    if i < len(L):
        res[i+j] = L[i]
        i += 1

    if j < len(R):
        res[i+j] = R[j]
        j += 1

    return res

def mergeKarrays(A,res=[]):
    k = len(A)
    if k < 2:
        return A
    if k == 2:
        res += merge(A[0],A[1])
        print(merge(A[0],A[1]))
        return merge(A[0],A[1])

    mid = k//2
    L = A[:mid]
    R = A[mid:]
    mergeKarrays(L,res)
    mergeKarrays(R,res)

    return res

arr = [[1,2,3],[2,3,4],[5,6,7],[4,5,6],[1,8,12,56],[123,231,800]]
print(mergeKarrays(arr))