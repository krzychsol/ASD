def findIdx(T,l,r,x):
    while r-l > 1:
        m = l + (r-l)//2
        if T[m] >= x:
            r = m
        else:
            l = m
    return r

def LIS(A):
    n = len(A)
    T = [0 for i in range(n+1)]
    T[0] = A[0]
    length = 1
    for i in range(1,n):
        if A[i] < T[0]:
            T[0] = A[i]
        elif A[i] >  T[length-1]:
            T[length] = A[i]
            length += 1
        else:
            T[findIdx(T,-1,length-1,A[i])] = A[i]

    return length


A = [2,3,7,8,7,4,12,9,10,11,5,1]
print(LIS(A))