from zad12ktesty import runtests 

"""
Zadanie 12 - Remont autostrady
Szablon rozwiązania: zad12k.py
W wyniku przewozu bardzo ciężkich części do potężnych maszyn, powstały niebezpieczne 
koleiny na długości całej autostrady. Z tego powodu musiała zostać ona natychmiast 
zamknięta, a prace remontowe powinny rozpocząć się jak najszybciej. Do przetargu stawiło
się k firm. Ze względów logistycznych prace zostały rozdzielone między różne gminy. Ilość 
kilometrów do wyremontowania w każdej z nich określa tablica T (tak, że i-ta gmina ma T[i] 
kilometrów autostrady). Zakładamy, że kolejne gminy w tablicy są ustawione obok siebie. 
Obowiązujące prawo nakazuje, że po zakończeniu remontu w danej gminie, firma albo musi 
zakończyć swoje prace i odebrać wynagrodzenie, albo może kontynuować pracę na 
kolejnym odcinku (tj., jeżeli remontowała odcinek i, teraz może remontować i+1, a dopiero po 
skończeniu jego kolejny, czyli i+2 itd.). Wyremontowanie jednego kilometra autostrady każdej 
z firm zajmuje jeden dzień. Zakładając, że wszystkie firmy zaczną remontować od swojej 
wskazanej gminy w tym samym momencie, a rządowi zależy, aby zakończyć remont jak 
najszybciej, napisz algorytm, który tak przydzieli początkowe gminy firmom, aby łączny czas 
remontu był jak najkrótszy (łączny czas to czas potrzebny do skończenia remontu firmie, 
której zajmie on najdłużej) 
Algorytm należy zaimplementować jako funkcję postaci:
def autostrada( T, k ):
 … 
która przyjmuje tablicę długości autostrad w gminach T oraz ilość firm k, które stawiły się do 
przetargu remontowego, a zwraca minimalny łączny czas (w dniach) potrzebny na remont.
Podpowiedź. Zakładając, że jest n gmin oraz k firm, oczekiwana złożoność czasowa dla 
algorytmu dynamicznego wynosi O(n2 
* k), a pamięciowa O(nk + n2
). (Problem da się 
rozwiązać też w złożoności czasowej O(nlogk) i pamięciowej O(1), co jednak odradzam)
Przykład. Dla danych:
T = [5, 10, 30, 20, 15]
k = 3
Wynikiem jest liczba 35
"""

def autostrada( T, k ):
    n = len(T)
    F = [[0 for _ in range(k+1)]for __ in range(n+1)]

    #dla k = 1
    for i in range(1,n+1):
        F[i][1] = sum(T[:i])

    #dla n = 1
    for i in range(1,k+1):
        F[1][i] = T[0]

    #od 2 do k
    for i in range(2,k+1):
        for j in range(2,n+1):
            minloc = float("inf")
            for p in range(1,j+1):
                minloc = min(minloc,max(sum(T[p:j]),F[p][i-1]))

            F[j][i] = minloc

    return F[n][k]

runtests ( autostrada,all_tests=True )