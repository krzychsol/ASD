"""
Zadanie 6:
Mamy daną tablicę z nominałami monet stosowanych w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm,
który oblicza minimalną ilość monet potrzebną do wydania
kwoty T (algorytm zachłanny, wydający najpierw największą monetę, 
nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako 8 + 5 + 1 + 1 zamiast 5 + 5 + 5). 
"""
#O(nT)

def coins(A,T):
    A = sorted(A) #sortuje nlogn
    dp = [0 for _ in range(T+1)] #tworze tablice gdzie pod indeksem i jest minimalna liczba monet potrzebna do wydania kwoty i
    for i in range(1,T+1):
        if i-A[0] >= 0: #jezeli najmniejszy niminal jest wiekszy niz kwota to bez sensu sprawdzac dalej
            MinVal = dp[i-A[0]] #zakladam ze mininalna ilosc nominalow jest dla pierwszego nominalu
            for nom in A: #sprawdzam dla reszty i minimalizuje
                if i-nom >= 0:
                    curr = dp[i-nom]
                    if curr < MinVal:
                        MinVal = curr
                else:
                    break
            dp[i] = MinVal+1

    return dp[T]

Banknots = [2,3,5,7,11,13]
value = 128
print(coins(Banknots,value))