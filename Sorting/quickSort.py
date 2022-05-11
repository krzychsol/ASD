from random import randint

def partition(A,p,r):
    i = p - 1
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A,p,r):
    if len(A) == 1:
        return A
    if p < r:
        pi = partition(A, p, r)
        quickSort(A, p, pi - 1)
        quickSort(A, pi + 1,r)

# Driver code to test above
A = [randint(1,100) for _ in range(randint(10,30))]
n = len(A)
print("Before quicksort: ",end="")
print(A)
quickSort(A, 0, n - 1)
print("After quicksort: ",end="")
print(A)


