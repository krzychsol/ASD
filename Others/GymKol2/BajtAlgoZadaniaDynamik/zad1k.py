from zad1ktesty import runtests
#O(n^2)

def roznica( S ):
    n = len(S)
    allOnes = True
    for i in range(n):
        if S[i] == '0':
            allOnes = False
            break

    if allOnes:
        return -1

    F = [[0 for _ in range(n)] for __ in range(n)]
    if S[0] == '0': F[0][0] = 1
    else: F[0][0] = -1

    for i in range(n):
        if S[i] == '0':
            F[i][i] = 1
        else:
            F[i][i] = -1
        for j in range(i+1,n):
            if S[j] == '0':
                diff = 1
            else:
                diff = -1
            F[i][j] = F[i][j-1]+diff

    maxRes = 0
    for el in F:
        if max(el) > maxRes:
            maxRes = max(el)
    return maxRes


runtests ( roznica )