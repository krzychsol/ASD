"""
    Masz daną tablicę zawierającą n (n >= 11) liczb naturalnych w zakresie [0, k]. Zamieniono 10 liczb z tej
    tablicy na losowe liczby spoza tego zakresu (np. dużo większe lub ujemne). Napisz algorytm, który
    posortuje tablicę w czasie O(n).

    Dzielimy tablicę na dwie - te "psujące" 10 elementów i te posortowane (pamiętamy o tym, żeby nie zmienić kolejności!). Sortujemy tę
    10-elementową tablicę (czymkolwiek, bo to czas stały) i je scalamy w czasie O(n).
"""


def merge(N,O):
    n = len(N)
    o = len(O)
    result = [0 for _ in range(n+o)]
    idx = 0
    idx_n = 0
    idx_o = 0

    while idx_n < n and idx_o < o:
        if N[idx_n] <= O[idx_o]:
            result[idx] = N[idx_n]
            idx_n += 1
        else:
            result[idx] = O[idx_o]
            idx_o += 1

        idx += 1

    while idx_n < n:
        result[idx] = N[idx_n]
        idx += 1
        idx_n += 1

    while idx_o < o:
        result[idx] = O[idx_o]
        idx += 1
        idx_o += 1

    return result

def sort(A,k):
    n = len(A)
    normal = [0 for _ in range(n-10)]
    out_of_range = [0 for _ in range(10)]

    idx_n = 0
    idx_o = 0
    for i in range(n):
        if 0 <= A[i] <= k:
            normal[idx_n] = A[i]
            idx_n += 1
        else:
            out_of_range[idx_o] = A[i]
            idx_o += 1

    out_of_range = sorted(out_of_range)
    return merge(normal,out_of_range)

arr=[2,12,2,88,40,6,34,60,60,70,45,80,90,8,8,9]
a=sort(arr,9)
print(a)
