"""
https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/

ZADANIE POLEGA NA ZNALEZIENIU MINIMALNEJ ILOSCI ZAMIAN POTRZEBNYCH DO POSORTOWANIA
TABLICY. BIERZEMY MINIMUM Z ILOSCI ZAMIAN PRZY SORTOWANIU ROSNACYM I MALEJACYM.
POMYSŁ Z GRAFEM : SZUKANIE CYKLI

ZLOZONOSC:
    - CZASOWA: O(NLOGN)
    - PAMIECIOWA: O(N)
"""

def lilysHomework(A):
    n = len(A)
    #SORTED ASCENDING ARRAY
    arrpos = [*enumerate(A)]
    arrpos.sort(key=lambda it: it[1])
    visited = [False for _ in range(n)]

    ans = 0
    for i in range(n):
        if visited[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans += cycle_size-1

    #SORTED DESCENDING ARRAY
    arrpos2 = [*enumerate(A)]
    arrpos2.sort(key=lambda it: it[1],reverse=True)
    visited = [False for _ in range(n)]

    ans2 = 0
    for i in range(n):
        if visited[i] or arrpos2[i][0] == i:
            continue
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = arrpos2[j][0]
            cycle_size += 1

        if cycle_size > 0:
            ans2 += cycle_size - 1

    return min(ans,ans2)

A = [7,3,15,12]
print(lilysHomework(A))