def medOfMed(A,i):
    n = len(A)

    # lista list 5 elementowych
    lists = [A[j:j+5] for j in range(0,n,5)]

    # lista median kazdej z list
    medians = [sorted(List)[len(List)//2] for List in lists]

    # szukam pivota mediany median
    if len(medians) <= 5:
        pivot = sorted(medians)[len(medians)//2]
    else:
        pivot = medOfMed(medians,len(medians)//2)

    #podzial na mniejsze i wieksze elementy od pivota
    low = [i for i in A if i < pivot]
    high = [i for i in A if i > pivot]

    x = len(low)
    if i < x:
        return medOfMed(low,i)
    elif i > x:
        return medOfMed(high,i-x-1)
    else:
        return pivot

A = [1,5,8,2,4,4]
print(medOfMed(A,3))