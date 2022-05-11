from zad2ktesty import runtests

"""
Zadanie 2 - Najdłuższy palindrom
Szablon rozwiązania: zad2k.py
Dany jest ciąg liter S. Proszę znaleźć taki SPÓJNY fragment tego podciągu, który będzie 
najdłuższym możliwym palindromem.
Algorytm należy zaimplementować jako funkcję postaci:
def palindrom( S ):
 … 
która przyjmuje ciąg S i zwraca ten najdłuższy palindrom.
Przykład. Dla ciągu:
aacaccabcc 
Wynikiem jest ciąg acca
"""

def palindrom( S ):
    n = len(S)
    F = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        F[i][i] = True

    for i in range(n-1):
        if S[i] == S[i+1]:
            F[i][i+1] = True
        else:
            F[i][i+1] = False

    k = 3
    while k<n:
        i = 0
        while i < n -k +1:
            j = i + k - 1
            if F[i+1][j-1] and S[i] == S[j]:
                F[i][j] = True
            i += 1
        k += 1

    maxLength = 0
    result = ""
    for i in range(n):
        for j in range(i+1,n):
            if F[i][j]:
                if j-i > maxLength:
                    maxLength = j-i
                    result = S[i:j+1]

    return result

runtests ( palindrom )