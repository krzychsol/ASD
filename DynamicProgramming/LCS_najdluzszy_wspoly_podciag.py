def LCS(X,Y):
    m = len(X)
    n = len(Y)
    curr = [None]*(n+1)

    for i in range(m+1):
        prev = curr[0]
        for j in range(n+1):
            backup = curr[j]
            if i == 0 or j == 0:
                curr[j] = 0
            else:
                if X[i-1] == Y[j-1]:
                    curr[j] = prev+1
                else:
                    curr[j] = max(curr[j],curr[j-1])
            print(curr, i, j)
            prev = backup

    return curr[n]

X = [2,1,5,4,2,5]
Y = [4,2,6,4,6]
if len(X) > len(Y):
    print(LCS(X,Y))
else:
    print(LCS(Y,X))