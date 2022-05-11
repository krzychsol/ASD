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
    tailIdx = [0 for _ in range(n + 1)]
    prevIdx = [-1 for i in range(n + 1)]

    length = 1
    for i in range(1, n):
        if A[i] < A[tailIdx[0]]:
            tailIdx[0] = i
        elif A[i] > A[tailIdx[length - 1]]:
            prevIdx[i] = tailIdx[length - 1]
            tailIdx[length] = i
            length += 1
        else:
            pos = GetCeilIndex(A, tailIdx, -1, length - 1, A[i])
            prevIdx[i] = tailIdx[pos - 1]
            tailIdx[pos] = i

    i = tailIdx[length - 1]
    result = []
    while i >= 0:
        result.append(A[i])
        i = prevIdx[i]

    result.reverse()
    lis_len = len(result)
    start = tailIdx[0]
    end = tailIdx[lis_len - 1]

    return result, start, end, tailIdx


def mr(X):
    n = len(X)

    increase, incStart, incEnd, incIdxList = LIS(X)
    X.reverse()
    decrease, decStart, decEnd, decIdxList = LIS(X)
    decrease.reverse()
    decStart = n - 1 - decStart
    decEnd = n - 1 - decEnd
    decStart, decEnd = decEnd, decStart
    X.reverse()

    secIncrease = []
    if decEnd < n - 1:
        secIncrease, inc2start, inc2End, inc2IdxList = LIS(X[decEnd + 1:])
        if X[decEnd] == X[inc2start]:
            secIncrease.pop(0)

    if len(increase) > len(decrease)+len(secIncrease):
        return increase

    return decrease+secIncrease

runtests(mr)
