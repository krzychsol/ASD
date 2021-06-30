from random import randint

#Program dostaje 3 tablice nieposortowane.
#Nalezy sprawdzic czy A+B = C dla pewnego i
#O(nlogn+mlogm+k(n+m))

def isthree(A,B,C):
    A.sort() #nlogn
    B.sort() #mlogm
    l = 0                              #left A array
    r = len(B) - 1                     #right B array
    for i in range(len(C)):
        while l<r:
            if A[l]+B[r] == C[i]:
                return (True,l,r,i)
            if A[l]+B[r] < C[i]:
                l += 1
            else:
                r -= 1
    return False

n = 30
m = 25
k = 20
A = [randint(1,40) for _ in range(n)]
B = [randint(1,100) for _ in range(m)]
C = [randint(1,60) for _ in range(k)]
print(isthree(A,B,C))
