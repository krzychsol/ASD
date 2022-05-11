'''Mamy daną tablicę A z n liczbami. Proszę zaproponować algorytm o złożoności O(n), który stwierdza,
czy w tablicy ponad połowa elementów ma jednakową wartość.'''


def bucketSearch(A, n):
    x = (n + 1) // 2 + 1

    maxVal = max(A)
    buckets = [[0] for _ in range(n + 1)]
    for i in range(n):
        normVal = A[i] / maxVal
        bucketIdx = int(n * normVal)
        buckets[bucketIdx][0] += 1
        if buckets[bucketIdx][0] >= x:
            return True

    return False

A = [1,1,1,0,3,2,2,2]
print(bucketSearch(A,8))