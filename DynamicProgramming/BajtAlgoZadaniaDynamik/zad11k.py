from zad11ktesty import runtests

"""
Zadanie 11 - Kontenerowiec
Szablon rozwiązania: zad11k.py
W porcie na odbiór oczekuje n kontenerów z towarem. Waga każdego kontenera jest znana i 
zapisana w tablicy T (w kilogramach). Dwuczęściowy kontenerowiec, który przypłynął 
odebrać towar jest ogromny - na tylko jednej z jego części zmieściłyby się wszystkie 
oczekujące kontenery. Jednak ze względów technicznych, aby statek nie zatonął, w każdej z 
dwóch jego części musi znajdować się towar o tej samej łącznej wadze. Z tego względu 
władze portowe muszą zaopatrzyć statek w pewną ilość kilogramowych odważników, które 
pozwolą na wyrównanie wagi w obydwu jego częściach. Odważniki te jednak są drogie, więc 
zależy im na tym, aby użyć ich jak najmniej. Twoim zadaniem jako programisty jest napisanie 
programu, który policzy, jaka jest ta najmniejsza możliwa liczba odważników.
Algorytm należy zaimplementować jako funkcję postaci:
def kontenerowiec( T ):
 … 
która przyjmuje tablicę wag kontenerów T i zwraca najmniejszą konieczną liczbę 
odważników, które trzeba umieścić na statku.
Przykład. Dla danych:
T = [1, 6, 5, 11]
Wynikiem jest liczba 1

"""

def f(T,F,i,p1,p2):
    if i == len(T):
        return 0
    if i == len(T)-1:
        p2 = sum(T[:i+1])-p1
        return abs(p1-p2)

    if F[i][p1] != float("inf"):
        return F[i][p1]

    p2 = sum(T[:i+1])-p1
    F[i][p1] = min(f(T,F,i+1,p1+T[i],p2),f(T,F,i+1,p1,p2+T[i]))

    return F[i][p1]

def kontenerowiec(T):
    n = len(T)
    suma = sum(T)
    F = [[float("inf") for _ in range(suma+1)]for __ in range(n)]
    w = f(T,F,0,0,0)

    return w

T =[1,6,11,5]
#kontenerowiec(T)
runtests ( kontenerowiec )
    