def distancesum(A):
    n = len(A)
    res = 0
    sum = 0
    for i in range(n):
        res += (A[i] * i - sum)
        sum += A[i]

    return res

A = [-1,0,1]
print(distancesum(A))