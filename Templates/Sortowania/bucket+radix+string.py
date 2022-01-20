def countSort(A,exp):
    n = len(A)
    R = [0 for _ in range(n)]

    #initialize count array
    C = [0 for _ in range(10)] #max A +1

    #store the count of each element in count array
    for i in range(n):
        idx = (A[i][1] / exp)
        C[int(idx%10)] += 1

    #store the cummulative count
    for i in range(1,10):
        C[i] += C[i-1]

    #Find the index of each element of the original array in count array
    #place the elements in output array
    i = len(A)-1
    while i>=0:
        idx = (A[i][1]/exp)
        R[C[int(idx%10)]-1] = A[i]
        C[int(idx%10)] -= 1
        i -= 1

    #Copy the sorted elements into original array
    for i in range(n):
        A[i] = R[i]

def radixSort(T):
    maxl = 0
    for i in range(n):
        if T[i][0] > maxl:
            maxl = T[i][0]

    exp = 1
    while maxl/exp>0:
        countSort(T,exp)
        exp *= 10

def insertionSort(A):
    n = len(A)
    for i in range(1,n):
        key = A[i]
        j = i-1
        while j>=0 and A[j][0] > key[0]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

def bucketSort(T):
    n = len(T) #dlugosc tablicy
    maxl = 0
    minl = n
    for i in range(n):
        if T[i][0] > maxl:
            maxl = T[i][0]
        if T[i][0] < minl:
            minl = T[i][0]

    norm = maxl - minl
    B = [[] for _ in range(n)] #tworze n kubelkow

    for i in range(n):
        norm_el = (T[i][0]-minl)/norm #normalizuje el do [0,1)
        bidx = int(norm_el*n) #wsadzam do odp kubleka
        if bidx != n:
            B[bidx].append(T[i])
        else:
            B[bidx-1].append(T[i])

    for i in range(n): #sortuje kubelki
        B[i] = insertionSort(B[i])

    idx = 0
    for i in range(n): #lacze kubelki i daje do wejsciowej tablicy
        for j in range(len(B[i])):
            T[idx] = B[i][j]
            idx+=1

    return T

# Driver Code
n = 8
T = ["ala","olga","ula","maciek","ulga","algo","mango","kot"]
A = [(0,0) for _ in range(n)]
for i in range(n):
    A[i] = (len(T[i]),T[i])

print(bucketSort(A))
print(radixSort(A))