def countsort(A, n, exp):
    output = [0 for _ in range(n)]
    count = [0 for _ in range(n)]

    for i in range(n):
        count[(A[i] // exp) % n] += 1

    for i in range(1, n):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        output[count[(A[i] // exp) % n] - 1] = A[i]
        count[(A[i] // exp) % n] -= 1

    for i in range(n):
        A[i] = output[i]


def sort(A, n):
    countsort(A, n, 1)
    countsort(A, n, n)
    return A


A = [40, 12, 45, 32, 33, 1, 22]
print(sort(A, len(A)))
