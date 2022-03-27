from random import randint

from random import randint


# porządek rosnący

def countingSort(arr):
    n = len(arr)
    k = max(arr)
    output = [0] * n  # tablica wyjsciowa tej samej wielkosci co wejsciowa
    count = [0] * (k + 1)  # potrzebujemy tablice do zliczenia o wielkosci k (tyle kluczy)

    for i in range(n):  # dla kazdej z wartosci w tablicy zwiekszam element o odpowiednim indeksie o 1
        count[arr[i]] += 1

    for i in range(1, k + 1):  # cumulative sum- teraz wartosc elementu o danym indeksie to ilosc elementow
        count[i] += count[i - 1]  # mniejszych badz rownych, co pozwoli zachowac stabilnosc algorytmu

    for i in range(n - 1, -1, -1):  # umieszczamy kazdy element z tablicy wejsciowej (od konca) w wyjsciowej
        output[count[arr[i]] - 1] = arr[i]  # -1 poniewaz indeksujemy od 0
        count[arr[i]] -= 1

    return output


# porządek malejący

def countingSort_descending(arr):
    n = len(arr)
    k = max(arr)
    output = [0] * n
    count = [0] * (k + 1)

    for i in range(n):
        count[arr[i]] += 1

    for i in range(k - 1, -1, -1):
        count[i] += count[i + 1]
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


arr = []
for i in range(7):
    arr.append(randint(0, 30))
print(arr)

print(countingSort(arr))

def count_num_in_range(A,a,b):
    n = len(A)
    R = [0 for _ in range(n)]

    #initialize count array
    C = [0 for _ in range(n)] #max A +1

    #store the count of each element in count array
    for i in range(n):
        C[A[i]] += 1

    #store the cummulative count
    for i in range(1,10):
        C[i] += C[i-1]

    print(C)
    return C[b]-C[a]

A = [randint(1,30) for i in range(20)]
print(A)
print(count_num_in_range(A,4,8))
