def matrix_chain_multiplication(p):
    n = len(p)
    m = [[0 for _ in range(n)]for __ in range(n)]
    s = [[0 for _ in range(n)]for __ in range(n)]

    for i in range(n):
        m[i][i] = 0

    for l in range(1,n):
        for srt in range(n-l):
            end = srt+l
            m[srt][end] = float("inf")
            for k in range(srt,end):
                q = m[srt][k] + m[k+1][end] + p[srt-1]*p[k]*p[end]
                if q < m[srt][end]:
                    m[srt][end] = q
                    s[srt][end] = k

    return m[0][n-1],s

def get_solution(s,i,j):
    if j == i:
        print(i,end="")
    else:
        print("(",end="")
        get_solution(s,i,s[i][j])
        get_solution(s,s[i][j]+1,j)
        print(")",end="")

P = [5,10,3,12,5,50,6]
res,ss = matrix_chain_multiplication(P)
get_solution(ss,1,len(P)-1)
print(res)