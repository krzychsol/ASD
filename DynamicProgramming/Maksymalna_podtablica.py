'''
podtablica spojna o najwiekszej sumie
'''

def maxsubarray(A):
    n = len(A)
    maxSoFar = 0
    maxEndingHere = 0

    for i in range(n):
        maxEndingHere += A[i]
        if maxEndingHere < 0:
            maxEndingHere = 0
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

    return maxSoFar

A = [-2,-3,4,-1,-2,1,8,-3]
print(maxsubarray(A))