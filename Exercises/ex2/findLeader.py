"""
Szukanie lidera w zbiorze w czasie O(n)
Lider to element występujący PONAD połowę razy w zbiorze.
"""

def findleader(A):
    n = len(A)
    cand = A[0]
    cnt = 1
    for i in range(1,n):
        if A[i] == cand:
            cnt += 1
        elif A[i] != cand:
            cnt -= 1
            if cnt == 0:
                cand = A[i]
                cnt = 1

    if cnt > 0:
        cnt = 0
        for i in range(n):
            if A[i] == cand:
                cnt += 1

    if cnt > n//2:
        return cand

    return False

A = [-1,1,2,2,2]
print(findleader(A))