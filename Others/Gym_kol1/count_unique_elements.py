"""
    Proszę zaimplementować funkcję:
    int count(arr);
    Funkcja ta przyjmuje na wejściu posortowaną tablicę n liczb całkowitych, w której mogą pojawiać się duplikaty.
    Funkcja powinna zliczać ilość wystąpień różnych wartości bezwzględnych elementów występujących w tej tablicy.
    Przykład:
    Wejście: {-1, -1, 0, 0, 1, 1, 1}
    Wyjście: 2
    Wejście: {1, 1, 1}
    Wyjście: 1

    Algorytm: Przechodzę liniowo jednocześnie od początku i końca tablicy.
    Ustawiam początkowo counter unikalnych elementów na rozmiar tablicy.
    Na bieżąco redukuje counter. Wykorzystuje fakt że tablica jest posortowana.
    Złożoność obliczeniowa: O(N)
    Złożoność czasowa: O(1)

"""
def count(arr):
    n = len(arr)
    i = 0
    j = n-1
    cnt = n

    while i < j:
        while i != j and arr[i] == arr[i+1]:
            i += 1
            cnt -= 1

        while i != j and arr[j] == arr[j-1]:
            j -= 1
            cnt -= 1

        if i == j:
            break

        sum = arr[i]+arr[j]
        if sum == 0:
            cnt -= 1
            i += 1
            j -= 1

        elif sum < 0:
            i += 1
        else:
            j -= 1

    return cnt


A = [-1,-1,-1,0,0,1,1,2,3]
print(count(A))