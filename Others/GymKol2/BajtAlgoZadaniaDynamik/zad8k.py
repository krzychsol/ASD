from zad8ktesty import runtests 

def napraw ( s, t ):
    n = len(s)
    k = len(t)

    F = [[0 for _ in range(n)]for __ in range(k)]
    if s[0] != t[0]:
        F[0][0] = 1

    for i in range(1,n):
        if s[i] != t[0]:
            F[0][i] = F[0][i-1]+1
        else:
            F[0][i] = F[0][i-1]

    for i in range(1,k):
        if t[i] != s[0]:
            F[i][0] = F[i-1][0]+1
        else:
            F[i][0] = F[i-1][0]

    for i in range(1,k):
        for j in range(1,n):
            if t[i] == s[j]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j-1],F[i-1][j],F[i][j-1])+1

    return F[k-1][n-1]

runtests ( napraw )