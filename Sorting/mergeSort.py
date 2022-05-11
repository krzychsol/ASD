from random import randint

def mergesort(T):
    n = len(T)
    if n <= 1:
        return T
    mid = len(T) // 2
    L = T[:mid]
    R = T[mid:]

    mergesort(L)
    mergesort(R)

    i = j = 0

    k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            T[k] = L[i]
            i += 1
        else:
            T[k] = R[j]
            j += 1
        k += 1

    while i < len(L):
        T[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        T[k] = R[j]
        j += 1
        k += 1

    return T

n = 10
T = [randint(1, 10) for i in range(10)]

print("przed sortowaniem: T =", T)
T = mergesort(T)
print("po sortowaniu    : T =", T)
print(T)



