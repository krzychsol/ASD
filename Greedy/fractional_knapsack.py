def fractional_knapsack(A,w): #tablica krotek (waga,profit)
    n = len(A)
    B = [[0]*2 for _ in range(n)]
    for i in range(n):
        B[i][0] = i
        B[i][1] = A[i][1]/A[i][0]

    B = sorted(B,key=lambda x:x[1],reverse=True)
    profit = 0.0
    currWeight = w
    for item in B:
        print(profit)
        if currWeight > 0:
            idx = item[0]
            if A[idx][0] <= currWeight:
                profit += A[idx][1]
                currWeight -= A[idx][0]
            else:
                profit += currWeight*A[idx][1]/A[idx][0]
                currWeight = 0

    return profit

T = [(1,5),(5,6),(3,9),(4,16)]
print(fractional_knapsack(T,10))
