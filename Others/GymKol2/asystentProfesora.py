"""
Asystent znanego profesora otrzymał polecenie wyliczenia sumy pewnego ciągu liczb (liczby mogą być zarówno dodatnie jak i ujemne):
n1+n2+...+nk. Aby zminimalizować błędy zaokrągleń asystent postanowił wykonać powyższe dodawania w takiej kolejności, by największy
co do wartości bezwzględnej wynik tymczasowy (wynik każdej operacji dodawania; wartość końcowej sumy również traktujemy jak wynik tymczasowy)
był możliwie jak najmniejszy.  Aby  ułatwić  sobie  zadanie,  asystent  nie  zmienia  kolejności  liczb  w  sumie  a  jedynie wybiera kolejność
dodawań. Napisz funkcję, która przyjmuje tablicę liczb n1, n2, . . . , nk (w kolejności w jakiej występują w sumie; zakładamy, że tablica
zawiera co najmniej dwie liczby) i zwraca największą wartość bezwzględną  wyniku  tymczasowego  w  optymalnej  kolejności  dodawań.  Na  przykład
dla  tablicy wejściowej: [1,−5,2] funkcja powinna zwrócić wartość 3, co odpowiada dodaniu −5 i 2 a następnie dodaniu 1 do wyniku.
"""

def min_abs_val(a,b):
    if abs(a) <= abs(b):
        return a
    return b

def max_abs_val(a,b):
    if abs(a) >= abs(b):
        return a
    return b

def opt_sum(A):
    n = len(A)
    prefix = [0 for _ in range(n+1)]
    prefix[0] = 0

    for i in range(1,n+1):
        prefix[i] = prefix[i-1]+A[i-1]

    memo = [[0 for _ in range(n)]for __ in range(n)]
    # w memo[i][j] zapamiętujemy wartość sumy tymczasowej, której wartość bezwzględna
    # na danym przedziale jest minimalna (z maksymalnych)

    for length in range(1,n):
        for start in range(n-length):
            end = start+length
            memo[start][end] = prefix[end+1] - prefix[start]

            best = float("inf")
            for k in range(start,end):
                best = min_abs_val(max_abs_val(memo[start][k],memo[k+1][end]),best)

            memo[start][end] = max_abs_val(best,memo[start][end])

    return abs(memo[0][n-1])

print(opt_sum([1,-5,2]))