
def countsort(A,i):
    n = len(A)
    letters = ord('z')-ord('a')+1
    C = [0]*letters
    B = [0]*len(A)

    for string in A:
        C[ord(string[i])-ord('a')] += 1

    for j in range(1,letters):
        C[j] += C[j-1]

    for p in range(n-1,-1,-1):
        C[ord(A[p][i])-ord('a')] -= 1
        B[C[ord(A[p][i])-ord('a')]] = A[p]

    for i in range(n):
        A[i] = B[i]

def radixsort(A):
    for i in range(len(A[0])-1,-1,-1):
        countsort(A,i)

def maketuples(A):
    n = len(A)
    for i in range(n):
        A[i] = (len(A[i]),A[i])
    return A

def bucketsort(A):
    n = len(A)
    Max = 0
    A = maketuples(A)

    for i in range(n):
        Max = max(Max,A[i][0])

    buckets = [[] for _ in range(Max+1)]
    for i in range(n):
        buckets[A[i][0]].append(A[i][1])

    cnt = 0
    for bucket in buckets:
        cnt += 1
        if len(bucket) > 0:
            radixsort(bucket)

    output = []
    for bucket in buckets:
        output.extend(bucket)

    return output

A = ["ala","ola","kota","stroma","ma","gol","ula","skwer","sztos"]
print(bucketsort(A))