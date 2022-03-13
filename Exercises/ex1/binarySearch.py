def binary_search(T,val):
    left = 0
    right = len(T)-1

    while left < right:
        mid = (left + right) // 2
        if T[mid] < val:
            left = mid+1
        else:
            right = mid

    if T[right] == val:
        return right
    return None

A = [10,15,17,30,31]
print(binary_search(A,32))
