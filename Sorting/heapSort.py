from random import randint

# Python program for implementation of heap Sort
# To heapify subtree rooted at index i.
# n is size of heap

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def heapify(A, n, i):
    largest = i  # Initialize largest as root
    l = left(i)  # left = 2*i + 1
    r = right(i)  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and A[largest] < A[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and A[largest] < A[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        A[i], A[largest] = A[largest], A[i]  # swap

        # Heapify the root.
        heapify(A, n, largest)

# The main function to sort an array of given size
#Sort O(n*ln(n))

def heapSort(A):
    n = len(A)

    # Build a maxheap.
    for i in range(n - 1, -1, -1):
        heapify(A, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(A, i, 0)

# Driver code
A = [randint(1,100) for _ in range(randint(10,30))]
n = len(A)
print("Before heapsort: ",end="")
print(A)
heapSort(A)
print("After heapsort: ",end="")
print(A)
