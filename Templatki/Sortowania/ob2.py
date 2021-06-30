def count_sort(T, n, key):
    C = [0 for _ in range(n)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[key(T[i])] += 1

    for i in range(1, n):
        C[i] += C[i - 1]

    for i in range(n-1, -1, -1):
        C[key(T[i])] -= 1
        B[C[key(T[i])]] = T[i]

    return B

def radix_sort(T, n):
    T = count_sort(T, n, lambda x: x % n)
    T = count_sort(T, n, lambda x: x // n)
    return T

T = [5, 2, 7, 3, 9]

print(radix_sort(T, 5))