from zad3ktesty import runtests

"""
Zadanie 3 - Najmniejsza k-ładna suma 
Szablon rozwiązania: zad3k.py
Dla każdego ciągu n liczb możemy obliczyć k-ładną sumę (Zakładamy, że k <= n). Poprzez 
k-ładną sumę rozumiemy minimalną sumę pewnych liczb wybranych w ten sposób, że z 
każdych k kolejnych elementów wybraliśmy przynajmniej jeden z nich (w szczególności 
oznacza to, że dla k=1 musimy wybrać wszystkie elementy, a dla k=n wystarczy wybrać 
jeden, najmniejszy z nich). Proszę napisać algorytm, który dla zadanej tablicy liczb 
naturalnych oraz wartości k oblicza k-ładną sumę. 
Algorytm należy zaimplementować jako funkcję postaci:
def ksuma( T, k ):
 … 
która przyjmuje tablicę liczb naturalnych T = [a1, a2, …, an] oraz liczbę naturalną k.
Przykład. Dla tablicy:
[1, 2, 3, 4, 6, 15, 8, 7] oraz k = 4
Wynikiem jest liczba 7
"""

def ksuma( T, k ):
    n = len(T)

    F = [float("inf") for _ in range(n+1)]
    for i in range(1,k):
        F[i-1] = T[k-1]
    for i in range(k-1,n+1):
        for j in range(i-k-1,i):
            F[i] = min(F[i],F[j]+T[i-1])
    print(F)
    return F[n]
T = [1, 2, 3, 4, 6, 15, 8, 7]
print(ksuma(T,4))
#runtests ( ksuma )