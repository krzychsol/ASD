from random import randint

def count_num_in_range(A,a,b):
    n = len(A)
    R = [0 for _ in range(n)]

    #initialize count array
    C = [0 for _ in range(n)] #max A +1

    #store the count of each element in count array
    for i in range(n):
        C[A[i]] += 1

    #store the cummulative count
    for i in range(1,10):
        C[i] += C[i-1]

    print(C)
    return C[b]-C[a]

A = [randint(1,30) for i in range(20)]
print(A)
print(count_num_in_range(A,4,8))
