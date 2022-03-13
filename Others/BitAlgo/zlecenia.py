def findMaximizedCapital(k,W,P,C):
    while k > 0 and C:
        max_cap = max(C)
        if W >= max_cap:
            if k >= len(C):
                W += sum(P)
            else:
                for i in range(k):
                    W += P.pop((i := P.index(max(P))))
            break
        else:
            imaxp = float("inf")
            for i in range(len(C)):
                if W >= C[i]:
                    if imaxp == float("inf"):
                        imaxp = i
                    else:
                        if max(P[imaxp],P[i]) == P[i]:
                            imaxp = i
            if imaxp != float("inf"):
                W +=  P.pop(imaxp)
                C.pop(imaxp)
                k -= 1
            else:
                break
    return W

k = 2
W = 0
P = [1, 2, 3]
C = [0, 1, 1]
print(findMaximizedCapital(k,W,P,C))