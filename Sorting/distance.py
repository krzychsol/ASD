'''
    Dane jest n punktów na osi liczbowej jednowymiarowej. Napisz algorytm, który stwierdzi,
    w którym z nich należy wybudować dom, tak aby suma euklidesowych odległości od tego punktu
    do wszystkich pozostałych była minimalna. Należy zwrócić również tę sumę.
    Algorytm powinien być jak najszybszy.
'''

# ALGORYTM

'''
    Najpierw sortujemy punkty. Później będziemy używać dwóch sum odległości (elementów tablicy): 
    wcześniejszych od aktualnego (prefix) oraz późniejszych od aktualnego (suffix). Dzięki nim wystarczy 
    jedno przejście po tablicy, a będziemy cały czas znali odległości do wcześniejszych i późniejszych elementów.
	Dla i-tego elementu wcześniejsze elementy mają położenia 
    A[0], A[1], … , A[i-1], a późniejsze A[i+1], A[i+2], …, A[n - 1].
    Suma odległości do wcześniejszych punktów to  (A[i] - A[0]) + (A[i] - A[1]) + … + (A[i] - A[i - 1]), czyli:
    i * A[i] - (A[0] + A[1] + … + A[i - 1]). Analogicznie dla elementów późniejszych.
	Zauważmy, że jeżeli będziemy trzymali “aktualny” prefix i suffix, czyli “aktualną” sumę elementów 
    wcześniejszych i późniejszych, to wzory sprowadzają się do i * A[i] - prefix oraz suffix - (len(a) - i - 1) * A[i]. 
    Dlatego też podczas iteracji po tablicy na początku prefix = 0, suffix = sum(arr)-A[0], a potem będziemy zwiększać prefix i 
    zmniejszać suffix o A[i], przechodząc dalej. W ten sposób będziemy mieli w pamięci O(1) i kosztem czasowym O(1) aktualną 
    sumę elementów wcześniejszych i późniejszych.
	Policzenie odległości sprowadza się do zastosowania wcześniej wyprowadzonych wzorów: dodajemy odległości do 
    elementów wcześniejszych i do elementów późniejszych, nadążamy za tym dla którego indeksu i jest ona najmniejsza 
    i to zwracamy.

    Złożoność: O(nlog(n)) ze względu na sortowanie, sama ta iteracja to O(n)
'''

def partition(A,p,r):
    i = p - 1
    pivot = A[r]

    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quickSort(A,p,r):
    if len(A) == 1:
        return A
    if p < r:
        pi = partition(A, p, r)
        quickSort(A, p, pi - 1)
        quickSort(A, pi + 1,r)

def distance(A):
    n = len(A)
    quickSort(A,0,n-1)

    prefix = 0
    suffix = sum(A) - A[0]
    curr_sum = suffix - (n - 1) * A[0]
    curr_idx = 0

    for i in range(1, n):
        prefix += A[i - 1]
        suffix -= A[i - 1]
        if i * A[i] - prefix + suffix - (n - 1 - i) * A[i] < curr_sum:
            curr_sum = i * A[i] - prefix + suffix - (n - 1 - i) * A[i]
            curr_idx = i

    return curr_idx, curr_sum
