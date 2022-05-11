from zad4ktesty import runtests

"""
Zadanie 4 - Ścieżka Falisza
Szablon rozwiązania: zad4k.py
Dana jest mapa wyrażona poprzez tablicę dwuwymiarową wymiarów N x N zawierająca 
liczby naturalne. Król Falisz znajduje się na polu (0,0) tej tablicy. Jego celem jest dojście do 
pola (n-1, n-1) i w trakcie tego procesu oblanie jak najmniejszej liczby studentów (każde pole 
tablicy wyraża ilość studentów, która zostanie oblana, gdy król przejdzie przez to pole). Ze 
względu na regulamin studiów Falisz może poruszać się jedynie o 1 pole w prawo lub w dół. 
Proszę napisać algorytm, który określi jaka jest minimalna liczba studentów, która zostanie 
oblana aby król doszedł do celu. Dla ułatwienia zadania pola (0, 0) oraz (n-1, n-1) przyjmują 
stałą wartość 0.
Algorytm należy zaimplementować jako funkcję postaci:
def falisz( T ):
 … 
która przyjmuje dwuwymiarową tablicę liczb naturalnych T i zwraca liczbę będącą minimalną 
ilością studentów, których król musi oblać.
Przykład. Dla tablicy:
T = [
 [0, 5, 4, 3],
 [2, 1, 3, 2],
 [8, 2, 5, 1],
 [4, 3, 2, 0]
]
Wynikiem jest liczba 9

"""

def falisz ( T ):
    n = len(T)
    F = [[0 for _ in range(n)]for __ in range(n)]
    F[0][0] = T[0][0]
    for i in range(1,n):
        F[0][i] = F[0][i-1]+T[0][i]
        F[i][0] = F[i-1][0]+T[i][0]

    for i in range(1,n):
        for j in range(1,n):
            F[i][j] = min(F[i-1][j]+T[i][j],F[i][j-1]+T[i][j])

    return F[n-1][n-1]

runtests ( falisz )
