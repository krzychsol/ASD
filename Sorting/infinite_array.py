"""
    Dana jest nieskończona tablica A, gdzie pierwsze n pozycji zawiera posortowane liczby naturalne,
    a reszta tablicy ma wartości None. Nie jest dana wartość n. Przedstaw algorytm, który dla danej
    liczby naturalnej x znajdzie indeks w tablicy, pod którym znajduje się wartość x. Jeżeli nie ma
    jej w tablicy, to należy zwrócić None.
"""

# ALGORYTM

'''
    Fajnie byłoby użyć wyszukiwania binarnego, ale problemem jest to, że nie znamy prawej 
    granicy liczb. Można ją szybko znaleźć, stosując prostą iterację: skaczemy o i do przodu, 
    sprawdzamy czy jesteśmy na wartości None lub wartości > x - jeżeli tak, to ta pozycja jest naszym prawym końcem 
    i zaczynamy binary search, w przeciwnym wypadku i *= 2 i skaczemy znowu. W ten sposób robimy takie skakanie 
    o kolejne potęgi liczby 2, dzięki czemu w log(n) znajdziemy prawy koniec (być może przeskoczymy n-ty indeks, 
    wchodząc na None, ale nie zaszkodzi to rzędowi złożoności). 
    Następnie wykonujemy binary search, szukając x. 

    Dostajemy ostatecznie O(log(n)).
'''


def binsearch(A,k,x):
    p = 0
    while p <= k:
        mid = (k-p)//2
        if A[mid] == x:
            return mid
        elif A[mid] is None or A[mid] > x:
            k = mid-1
        else:
            p = mid+1
    return None


def search(A,x):
    i = 1
    while A[i] is not None and A[i] <= x:
        i *= 2
    return binsearch(A,i,x)