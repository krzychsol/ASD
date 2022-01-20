from random import randint

#COMPLEXIBILITY [ O(nlogk) ]
#MOZNA ZASOTOSOWAC HEAPSORTA-MIN 
#MERGE K ARRAYS---------------------------------------------------------------------

def merge2arrays(L,R):
    res = []
    i = 0
    j = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            res.append(L[i])
            i += 1
        else:
            res.append(R[j])
            j += 1

    if i < len(L):
        res.extend(L[i:])
    if j < len(R):
        res.extend(R[j:])

    return res

def mergeKarrays(arr,res=[]):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        res += merge2arrays(arr[0], arr[1])
        return merge2arrays(arr[0],arr[1])
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]
    mergeKarrays(L,res)
    mergeKarrays(R,res)
    return res

#DRIVER CODE--------------------------------------------------------------------------

arr = [[1,2,3],[2,3,4],[5,6,7],[4,5,6],[1,8,12,56],[123,231,800]]
print(mergeKarrays(arr))

