#zad 2
def contain(A, a):
    if A[0] >= a[0] and A[1] <= a[1]:
        return True

def lego(T):
    n = len(T)
    F = [1] * (n+1)
    for i in range(1, n):
        for j in range(i):
            if contain(T[i], T[j]):
                if F[j] + 1 > F[i]:
                    F[i] = F[j] + 1
    return n - max(F)


#test
T = [[1, 5], [4, 5], [1, 2], [2, 5], [4.5, 5]]
print(lego(T))