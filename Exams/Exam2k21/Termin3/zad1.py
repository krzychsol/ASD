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
    return result,tailIdx

def mr(X):
    inc,incIdx = LIS(X)
    X.reverse()
    dec,decIdx = LIS(X)
    dec.reverse()
    #print(dec,inc)
    incFirst = incIdx[0]
    incLast = incIdx[len(incIdx)-1]
    decLast = decIdx[len(decIdx)-1]
    len_dec = len(dec)
    len_inc = len(inc)

    if decLast == incFirst:
        result_len = len_dec + len_inc
        result_mr = dec + inc

        if dec[len_dec - 1] == inc[0]:
            result_len -= 1
            result_mr[len_dec] = float("inf")
            result_mr.remove(float("inf"))

    elif incFirst < decLast < incLast:
        result_len = len_dec + (len_inc - incFirst)


    #czy mozna skleic



    return result_mr


runtests(mr)
