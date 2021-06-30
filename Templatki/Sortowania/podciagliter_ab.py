from math import pow

def convert2dec(s):
    res = 0
    w = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'b':
            res += pow(2,w)
        w += 1
    return int(res)

def convert2str(x,k):
    s = ""
    while x:
        if x%2 == 0:
            s += '0'
        else:
            s += '1'
        x = x//2

    res = ""
    while len(s) < k:
        s += '0'
    for i in range(len(s)-1,-1,-1):
        if s[i] == '0':
            res += 'a'
        else:
            res += 'b'

    return res

def subsuequnce(s,k):
    n = len(s)
    A = [0 for i in range(n-k+1)]
    i = 0
    while i+k<=n:
        A[i] = convert2dec(s[i:i+k])
        i+=1

    C = [0 for _ in range(max(A)+1)]
    for i in range(n-k+1):
        C[A[i]]+=1

    idx = 0
    for i in range(n-k+1):
        if C[i] == max(C):
            idx = i
            break

    return convert2str(idx,k)

s = "ababaaaabb"
k = 3
print(subsuequnce(s,k))
