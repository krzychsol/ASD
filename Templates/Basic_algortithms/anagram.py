from random import randint

#ZLOZONOSC pamieciowa O(n+k)
def isanagram(a,b,k):
    poma = [0]*k
    pomb = [0]*k
    for i in range(len(a)):
        poma[a[i]] += 1
    for i  in range(len(b)):
        pomb[b[i]] += 1

    for i in range(k):
        if (poma[i]!=pomb[i]):
            return False
    return True

def allocate(n):
    return [randint(1000) for i in range(n)]

#ZLOZONOSC pamieciowa O(n)
def isanagram2(a,b,k):
    T = allocate(k)
    for el in a:
        T[el] = 0
    for el in b:
        T[el] = 0

    for el in a:
        T[el] += 1
    for el in b:
        T[el] -= 1

    for el in a:
        if T[el] != 0:
            return False
    for el in b:
        if T[el] != 0:
            return False

    return True

a = "kajak"
b = "kajak"
