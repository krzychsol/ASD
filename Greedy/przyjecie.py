def inviteList(A):
    n = len(A)
    maxN=0
    for i in range(n):
        maxN = max(maxN,A[0],A[1])

A = [[0,1],[0,2],[1,5],[2,3]]