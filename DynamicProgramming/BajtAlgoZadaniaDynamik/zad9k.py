from zad9ktesty import runtests
from math import inf

"""
Zadanie 9 - Ładowanie promu (ze zwracaniem)
Szablon rozwiązania: zad9k.py
Dana jest tablica P z długościami samochodów (w umownej jednostce) które oczekują w 
kolejce, aby wjechać na prom. Pierwszy oczekujący samochód znajduje się pod zerowym 
indeksem. Prom ma dwa pokłady (górny i dolny) o długościach odpowiednio wyrażonych 
jako g i d. Zakładamy, że pojazdy mogą parkować "zderzak w zderzak" tj. bez zachowania 
odstępów między sobą. Każdy pojazd może wjechać na dowolnie wybrany z pokładów, 
jednak nie może wyprzedzić poprzedzających go samochodów. Niestety nie zawsze znajdzie 
się miejsce dla kolejnego samochodu. W takiej sytuacji kierowca ostatniego pojazdu, 
któremu udało się wjechać na prom, zgodnie z tradycją musi zamknąć wjazd oraz sporządzić 
listę obecności pojazdów TYLKO na swoim pokładzie w kolejności wjazdu pojazdów na ten 
pokład (W szczególności kierowca ten będzie ostatnim na liście obecności). Jako informatyk 
pracujący w biurze portowym, zostałeś poproszony o napisanie programu, który wskaże jak 
należy wpuszczać samochody na prom (tj. który samochód skierować na który pokład), aby 
ich łączna ilość na promie była jak największa.
Algorytm należy zaimplementować jako funkcję postaci:
def prom( P, g, d ):
 … 
która przyjmuje tablicę długości pojazdów P = [p1, p2, …, pn] oraz długości pokładów g oraz 
d, a zwraca posortowaną tablicę indeksów pojazdów znajdujących się na liście obecności.
Przykład. Dla danych:
T = [5, 6, 1, 3, 2, 4, 3, 5]
l1 = 8
l2 = 10
Wynikiem jest między innymi tablica [1, 4]
Uw. Może być wiele poprawnych wyników
"""


def f(P,DP,g,d,i):
    if i == len(P):
        return 0

    if DP[i][g][d] != -1:
        return DP[i][g][d]

    if P[i] > g and P[i] > d:
        DP[i][g][d] = 0
        return 0

    if P[i] > g:
        DP[i][g][d] = f(P,DP,g,d-P[i],i+1)+1
    elif P[i] > d:
        DP[i][g][d] = f(P,DP,g-P[i],d,i+1)+1
    else:
        res1 = f(P,DP,g-P[i],d,i+1)
        res2 = f(P,DP,g,d-P[i],i+1)
        DP[i][g][d] = max(res1,res2)+1

    return DP[i][g][d]


def prom(P, g, d):
    n = len(P)
    DP = [[[-1 for _ in range(d+1)]for __ in range(g+1)]for ___ in range(n)]
    w = f(P,DP,g,d,0)

    i = 0
    g = g
    d = d
    sol1 = []
    sol2 = []
    while i < n and (P[i] <= d or P[i] <= g):
        if P[i] > d:
            wd = 0
            wg = 1
        elif P[i] > g:
            wd = 1
            wg = 0
        else:
            wd = f(P,DP,g,d-P[i],i+1)
            wg = f(P,DP,g-P[i],d,i+1)

        if wd > wg:
            sol1.append(i)
            d -= P[i]
        else:
            sol2.append(i)
            g -= P[i]

        i+=1

    if w-1 in sol1:
        return sol1
    return sol2



T = [5,6,1,3,2,4,3,5]
g = 8
d = 10
#print(prom(T,g,d))
runtests ( prom )