def sortwave(A):
    n = len(A)
    for i in range(0, n, 2):
        if i > 0 and A[i] < A[i - 1]:
            A[i], A[i - 1] = A[i - 1], A[i]

        if i < n - 1 and A[i] < A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]

    return A

A = [1, 2, 3, 4, 5, 6 ,7 ]
print(sortwave(A))