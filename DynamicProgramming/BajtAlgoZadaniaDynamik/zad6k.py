from zad6ktesty import runtests 

"""
Zadanie 6 - Hasło do laptopa
Szablon rozwiązania: zad6k.py
Podczas Twoich praktyk zawodowych w biurze śledczym otrzymałeś zadanie dostania się do 
pewnego zabezpieczonego hasłem laptopa. Jedyną podpowiedzią jaką zostawił przestępca 
był pewien ciąg cyfr wyrażony jako string S. Odkryto już, że w rzeczywistości podpowiedź 
pozostawiona przez przestępcę była pewną tajną wiadomością, która została zakodowana 
poprzez zamienienie liter na znaki (tak np. A = 1, B = 2, …, Z = 26) oraz, że hasło ustawione 
przez przestępcę to tak naprawdę liczba wyrażająca całkowitą liczbę różnych wiadomości, 
które mogą ukrywać się pod zakodowanym ciągiem. Twoim zadaniem jest napisanie 
algorytmu, który zwróci poprawne hasło niezbędne do zalogowania się do laptopa. Możesz 
przyjąć, że pusty ciąg ma tylko 1 rozwiązanie, a niepoprawne wiadomości 0 rozwiązań 
(przez niepoprawne można uznać np. takie, które posiadają dwa zera pod rząd, z których nie 
da się odczytać żadnej litery)
Algorytm należy zaimplementować jako funkcję postaci:
def haslo( S ):
 … 
która przyjmuje string S i zwraca liczbę będącą poprawnym hasłem do laptopa.
Przykład. Dla ciągu znaków:
S = "123"
Wynikiem jest liczba 3 ponieważ zaszyfrowana wiadomość "123" może zostać zakodowane 
jako "ABC" (123), "LC" (12 3) lub "AW" (1 23)
"""

def haslo ( S ):
    if S == "":
        return 1

    n = len(S)
    for i in range(n-1):
        if S[i] == S[i+1] == "0":
            return 0

    F = [1 for _ in range(n)]
    if int(S[0]) == 0:
        F[0] = 0

    if S[0] == "1":
        F[1] = 2

    if S[0] == "2":
        if 0 <= int(S[1]) <= 6:
            F[1] = 2

    for i in range(2,n):
        if S[i-1] == "0":
            F[i] = F[i-1]+1
        if S[i-1] == "1":
            F[i] = F[i-1]+F[i-2]
        if S[i-1] == "2" and 0 <= int(S[i]) <= 6:
            F[i] = F[i-1]+F[i-2]
        else:
            F[i] = max(F[i],F[i-1])




    print(F)
    return F[n-1]

#S = "010"
#print(haslo(S))
runtests ( haslo )