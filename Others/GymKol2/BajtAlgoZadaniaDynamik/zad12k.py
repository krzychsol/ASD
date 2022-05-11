from zad12ktesty import runtests 

def autostrada( T, k ):
    n = len(T)
    F = [[0 for _ in range(k+1)]for __ in range(n+1)]

    #dla k = 1
    for i in range(1,n+1):
        F[i][1] = sum(T[:i])

    #dla n = 1
    for i in range(1,k+1):
        F[1][i] = T[0]

    #od 2 do k
    for i in range(2,k+1):
        for j in range(2,n+1):
            minloc = float("inf")
            for p in range(1,j+1):
                minloc = min(minloc,max(sum(T[p:j]),F[p][i-1]))

            F[j][i] = minloc

    return F[n][k]

runtests ( autostrada,all_tests=True )