def binsearch(A,x):
    n = len(A)
    l = 0
    r = n-1

    while l <= r:
        mid = (l+r)//2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            l = mid+1
        else:
            r = mid-1

    return None

def kclosest(A,x,k):
    n = len(A)
    crossidx = binsearch(A,x)
    left = crossidx - 1
    right = crossidx + 1
    result = [0 for _ in range(k)]
    residx = 0

    cnt = 0
    while cnt < k:
        if left < 0:
            result[residx] = A[right]
            right += 1
            residx += 1
            cnt += 1
        elif right >= n:
            result[residx] = A[left]
            left -= 1
            residx += 1
            cnt += 1
        else:
            if abs(A[crossidx]-A[left]) <= abs(A[crossidx]-A[right]):
                result[residx] = A[left]
                left -= 1
                residx += 1
                cnt += 1
            else:
                result[residx] = A[right]
                right += 1
                residx += 1
                cnt += 1
    return result


A = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]
print(kclosest(A,35,4))
