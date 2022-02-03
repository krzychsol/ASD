X = [0.25,0.5,1.6]

def minpokrycie(X):
    n = len(X)
    X.sort()
    cnt = 0
    i = 0

    while i < n:
        startX = X[i]
        idx = i+1
        while idx < n and X[idx] < startX+1.0:
            idx += 1

        cnt += 1
        i = idx

    return cnt

print(minpokrycie(X))