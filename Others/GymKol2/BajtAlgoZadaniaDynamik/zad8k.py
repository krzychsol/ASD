from zad8ktesty import runtests 

"""
Zadanie 8 - Zepsuty wyświetlacz
Szablon rozwiązania: zad8k.py
W pewnym mieście zepsuły się wyświetlacze pokazujące nazwy przystanków autobusowych 
(zakładamy, że są one jednym słowem, bez spacji). Jako, że informatycy nie mogli sobie 
poradzić z problemem, postanowiono, że wszystkie literówki zostaną poprawione ręcznie 
przez pracowników. Pracownik może naprawiać napis poprzez dodawanie do niego liter, 
usuwanie z niego liter lub zamienianie istniejących liter na inne. Aby zoptymalizować swoją 
pracę musi wiedzieć, jaką najmniejszą ilość operacji musi wykonać, aby naprawić 
wyświetlacz. Napisz algorytm, który zwróci minimalną liczbę operacji, która musi zostać 
wykonana przez pracownika w celu naprawienia wyświetlacza.
Algorytm należy zaimplementować jako funkcję postaci:
def napraw( s, t ):
 … 
która przyjmuje ciąg znaków s będący błędną nazwą przystanku na wyświetlaczu, oraz ciąg 
znaków t będący poprawna nazwą przystanku (do której uzyskania dążymy)
Przykład. Dla danych:
s = swidry
t = kawiory
Wynikiem jest liczba 3
"""

def napraw ( s, t ):
    n = len(s)
    k = len(t)

    F = [[0 for _ in range(n)]for __ in range(k)]
    if s[0] != t[0]:
        F[0][0] = 1

    for i in range(1,n):
        if s[i] != t[0]:
            F[0][i] = F[0][i-1]+1
        else:
            F[0][i] = F[0][i-1]

    for i in range(1,k):
        if t[i] != s[0]:
            F[i][0] = F[i-1][0]+1
        else:
            F[i][0] = F[i-1][0]

    for i in range(1,k):
        for j in range(1,n):
            if t[i] == s[j]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j-1],F[i-1][j],F[i][j-1])+1

    return F[k-1][n-1]

runtests ( napraw )