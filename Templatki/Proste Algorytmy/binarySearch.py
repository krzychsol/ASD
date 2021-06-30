A = [1,2,3,7,9,13,14]

def bin_search(val,A):
    left = 0
    right = len(A)-1
    while left < right:
        mid = (left+right)//2
        if A[mid] < val:
            left = mid+1
        else:
            right = mid
    if A[right] == val:
        return True
    else:
        return False

print(bin_search(15,A))