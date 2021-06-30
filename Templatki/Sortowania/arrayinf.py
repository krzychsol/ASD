from random import randint

def bin_search(val,A,l,r):
    left = l
    right = r
    while left < right:
        mid = (left+right)//2
        if A[mid] < val:
            left = mid+1
        else:
            right = mid
    if A[right] == val:
        return right
    else:
        return None

def find(T,x):
    i = 1
    if T[i] == None:
        return 0 if T[0] == x else None
    while T[i] != None and T[i] < x:
        i = i*2

    return bin_search(x,T,i//2,i)

n = 100
T = [randint(1,130) for _ in range(n)]
T.sort()
for i in range(50,n):
    T[i] = None
print(T)
print(find(T,17))