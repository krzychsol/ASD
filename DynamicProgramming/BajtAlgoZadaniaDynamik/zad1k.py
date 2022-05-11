from zad1ktesty import runtests

"""
Zadanie 1 - Największa różnica w podciągu
Szablon rozwiązania: zad1k.py
Dany jest ciąg binarny tj. zer oraz jedynek S. Proszę znaleźć taki SPÓJNY fragment tego 
ciągu, w którym różnica pomiędzy ilością zer, a jedynek, będzie jak największa. Jeżeli w 
ciągu występują same jedynki, należy założyć, że rozwiązaniem jest -1 
Algorytm należy zaimplementować jako funkcję postaci:
def roznica( S ):

która przyjmuje ciąg S i zwraca wyliczoną największą osiągalną różnicę.
Przykład. Dla ciągu:
11000010001
Wynikiem jest liczba 6
"""

#O(n^2)

def roznica( S ):
    n = len(S)
    allOnes = True
    for i in range(n):
        if S[i] == '0':
            allOnes = False
            break

    if allOnes:
        return -1

    F = [[0 for _ in range(n)] for __ in range(n)]
    if S[0] == '0': F[0][0] = 1
    else: F[0][0] = -1

    for i in range(n):
        if S[i] == '0':
            F[i][i] = 1
        else:
            F[i][i] = -1
        for j in range(i+1,n):
            if S[j] == '0':
                diff = 1
            else:
                diff = -1
            F[i][j] = F[i][j-1]+diff

    maxRes = 0
    for el in F:
        if max(el) > maxRes:
            maxRes = max(el)
    return maxRes


runtests ( roznica )