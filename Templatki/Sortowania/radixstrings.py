def radixsortstring(A):
    maxLen = -1
    for str in A: #znajduje najdluzszy string
        strLen = len(str)
        maxLen = max(maxLen,strLen)

    oa = ord('a')-1 #kod pierwszej litery
    oz = ord('z')-1 #kod ostatniej litery
    n = oz-oa+2 #ilosc kubelkow+pusta literka
    buckets = [[] for i in range(0,n)]

    for position in reversed(range(0,maxLen)):
        for str in A:
            idx = 0 #oznacza puste literki
            if position < len(str):
                idx = ord(str[position])-oa
            buckets[idx].append(str)

        del A[:]
        for bucket in buckets:
            A.extend(bucket)
            del bucket[:]
    return A

A = ["ala","arek","kaja","krzysiek","falisz","urszula","halina","ania","ala"]
radixsortstring(A)
print(A)