from Exams.Exam2k21.Termin3.zad1testy import runtests

def GetCeilIndex(arr, T, l, r, key):
    while r - l > 1:

        m = l + (r - l) // 2
        if arr[T[m]] >= key:
            r = m
        else:
            l = m

    return r

def LIS(A):
    n = len(A)
    tailIdx = [0 for _ in range(n+1)]
    prevIdx = [-1 for i in range(n+1)]

    length = 1
    for i in range(1,n):
        if A[i] < A[tailIdx[0]]:
            tailIdx[0] = i
        elif A[i] > A[tailIdx[length-1]]:
            prevIdx[i] = tailIdx[length-1]
            tailIdx[length] = i
            length += 1
        else:
            pos = GetCeilIndex(A,tailIdx,-1,length-1,A[i])
            prevIdx[i] = tailIdx[pos-1]
            tailIdx[pos] = i

    i = tailIdx[length - 1]
    result = []
    while i >= 0:
        result.append(A[i])
        i = prevIdx[i]


    result.reverse()
    return result

def mr(X):
    inc = LIS(X)
    print(inc)
    X.reverse()
    dec = LIS(X)
    dec.reverse()
    print(dec)

    return



T = [4, 10, 5, 1, 8, 2, 3, 4]
mr(T)
#runtests(mr)
