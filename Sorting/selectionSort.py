def select_sort(T):
    n = len(T)
    for i in range(n):
        k = i
        for j in range(i+1,n):
            if T[j] < T[k]:
                k = j
        T[k],T[i] = T[i],T[k]

T = [1,4,2,5,3,64,32,43]
select_sort(T)
print(T)
    