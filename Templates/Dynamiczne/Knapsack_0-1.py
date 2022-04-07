def knapsack(W,P,MaxW):
    n = len(W)
    F = [[0]*(MaxW+1) for _ in range(n)]
    for w in range(W[0],MaxW+1):
        F[0][w] = P[0]
    for i in range(1,n):
        for w in range(1,MaxW+1):
            F[i][w] = F[i-1][w]
            if w >= W[i]:
                F[i][w] = max(F[i][w],F[i-1][w-W[i]]+P[i])

    return F[n-1][MaxW],F

def getsolution(F,W,P,i,w):
    if i==0:
        if w >= W[0]:
            return [0]
        return []

    if w >= W[i] and F[i][w] == F[i-1][w-W[i]]+P[i]:
        return getsolution(F,W,P,i-1,w-W[i])+[i]
    return getsolution(F,W,P,i-1,w)

W = [5,10,3,7,15,50,1]
P = [2,8,30,1,100,12,10]
maxW = 15

maxP,F = knapsack(W,P,maxW)
print(maxP)
print(getsolution(F,W,P,len(W)-1,maxW-1))
