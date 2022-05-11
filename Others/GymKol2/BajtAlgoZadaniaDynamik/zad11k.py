from zad11ktesty import runtests

def f(T,F,i,p1,p2):
    if i == len(T):
        return 0
    if i == len(T)-1:
        p2 = sum(T[:i+1])-p1
        return abs(p1-p2)

    if F[i][p1] != float("inf"):
        return F[i][p1]

    p2 = sum(T[:i+1])-p1
    F[i][p1] = min(f(T,F,i+1,p1+T[i],p2),f(T,F,i+1,p1,p2+T[i]))

    return F[i][p1]

def kontenerowiec(T):
    n = len(T)
    suma = sum(T)
    F = [[float("inf") for _ in range(suma+1)]for __ in range(n)]
    w = f(T,F,0,0,0)

    return w

T =[1,6,11,5]
#kontenerowiec(T)
runtests ( kontenerowiec )
    