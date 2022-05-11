from zad10ktesty import runtests
from math import sqrt

"""
Zadanie 10 - Sklep z dywanami
Szablon rozwiązania: zad10k.py
Pewien przedsiębiorca potrzebuje zamówić do swojej firmy dywany o łącznym polu 
powierzchni wynoszącym N metrów kwadratowych. Nie martwi się on jakich będą one 
wymiarów, ponieważ może je w dowolny sposób przycinać i łączyć. Aczkolwiek sklep, w 
którym chce je kupić, sprzedaje tylko kwadratowe dywany o boku długości wyrażoną liczbą 
naturalną określającą długość w metrach. Koszt zapakowania każdego dywanu jest stały 
niezależnie od jego wielkości. Ze względów podatkowych przedsiębiorca potrzebuje 
zminimalizować łączny koszt zapakowania dywanów, które zakupi, jednocześnie dbając o 
środowisko nie może dopuścić, żeby jakikolwiek fragment dywanu się zmarnował. Twoim 
zadaniem jako jego pracownika jest stworzenie listy wymiarów dywanów (wyrażonych jako 
długość ich boku w metrach), które przedsiębiorca musi zakupić.
Algorytm należy zaimplementować jako funkcję postaci:
def dywany( N ):
 … 
która przyjmuje wymagane pole powierzchni dywanów N w metrach kwadratowych, a zwraca 
tablicę długości boków dywanów, które trzeba kupić.
Przykład. Dla danych:
N = 6
Wynikiem jest np. tablica [1, 1, 2]

"""

def dywany ( N ):

    F = [float("inf") for _ in range(N+1)]
    F[1] = 1
    F[0] = 0
    for i in range(2,N+1):
        j = 1
        minloc = F[i]
        while i-j*j >= 0:
            if F[i-j*j] != float("inf"):
                minloc = min(minloc,F[i-j*j])
            j+=1
        F[i] = minloc+1
    print(F)

    sol = []
    sum = N
    nums = F[N]


    while sum > 0 and nums > 0:
        if nums == 1:
            sol.append(int(sqrt(sum)))
            nums -= 1
            sum -= 1

        else:
            j = 1
            while sum - j*j > 0:
                if F[sum] == F[sum-j*j]+1:
                    sol.append(j)
                    nums -= 1
                    sum -= j*j
                    break
                j += 1

    return sol


#N = 18
#print(dywany(N))
runtests( dywany )

