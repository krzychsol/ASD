from zad10ktesty import runtests
from math import sqrt

def dywany ( N ):

    F = [float("inf") for _ in range(N+1)]
    F[1] = 1
    F[0] = 0
    for i in range(2,N+1):
        j = 1
        minloc = F[i]
        while i-j*j >= 0:
            if F[i-j*j] != float("inf"):
                minloc = min(minloc,F[i-j*j])
            j+=1
        F[i] = minloc+1
    print(F)

    sol = []
    sum = N
    nums = F[N]


    while sum > 0 and nums > 0:
        if nums == 1:
            sol.append(int(sqrt(sum)))
            nums -= 1
            sum -= 1

        else:
            j = 1
            while sum - j*j > 0:
                if F[sum] == F[sum-j*j]+1:
                    sol.append(j)
                    nums -= 1
                    sum -= j*j
                    break
                j += 1

    return sol


#N = 18
#print(dywany(N))
runtests( dywany )

