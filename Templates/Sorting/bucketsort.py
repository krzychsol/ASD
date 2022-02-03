def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def bucketSort(T):
    n = len(T)
    norm = max(T)-min(T)
    B = [[] for _ in range(n)] #tworze n kubelkow

    for el in T:
        norm_el = (el-min(T))/norm #normalizuje el do [0,1)
        bidx = int(norm_el*n) #wsadzam do odp kubleka
        if bidx != n:
            B[bidx].append(el)
        else:
            B[bidx-1].append(el)

    for i in range(n): #sortuje kubelki
        B[i] = insertionSort(B[i])

    idx = 0
    for i in range(n): #lacze kubelki i daje do wejsciowej tablicy
        for j in range(len(B[i])):
            T[idx] = B[i][j]
            idx+=1

    return T

# Driver Code
n = 7
x = [2,1,5,10,3,5,7]
print(x)
print(bucketSort(x))