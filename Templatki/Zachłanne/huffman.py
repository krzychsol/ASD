from queue import PriorityQueue

'''
Algorytm wyznacza kody Huffmana tworząc najpierw drzewo na podstawie częstości występowania każdego znaku.
Używa do tego celu kolejkę priorytetową działającą jako min-heap przez co przyspiesza czas działania algorytmu.
Po utworzeniu drzewa Huffmana algorytm rekurencyjnie tworzy kody Huffmana przesuwajac sie po gałęziach drzewa.
Po dotarciu do liscia wypisuje wynikowy kod Huffmana dla danego znaku oraz aktualizuje sumaryczną długość kodu.

Złożoność obliczeniowa:
Algorytm dzięki wykorzystaniu kolejki priorytetowej wstawia i usuwa z drzewa w czasie O(logn) względem ilości unikalnych znaków.
Zatem budowanie drzewa jest w czasie: O(nlogn).
Wypisywanie kodów działa w czasie O(n^2).
Zatem złożoność czasowa całego algorytmu to : 0(nlogn + n^2) co w notacji O daje 0(n^2).
'''

# Drzewo kodów Huffmana
class node:
    def __init__(self, freq, symbol,idx= None, left=None, right=None):
        # Częstość występowania znaku
        self.freq = freq

        # znak
        self.symbol = symbol

        # lewy potomek w drzewie
        self.left = left

        # prawy potomek w drzewie
        self.right = right

        # Wartość kodu {0,1}
        self.huff = ''

        # Numer indeksu w tablicy S
        self.idx = idx

    def isLeaf(self):  # pomocnicza metoda, która pozwoli określić, czy liść przechowuje znak
        return self.symbol != ""

    # funkcja __lt__ pomoże nam przy tworzeniu priority_queue
    def __lt__(self, other):
        if self.freq != other.freq:  # wykonujemy normalne porównanie, jeżeli liście są różne;
            return self.freq < other.freq
        if not self.isLeaf() and other.isLeaf():  # w przeciwnym wypadku ważniejsze są liście mające znak
            return True
        if self.isLeaf() and not other.isLeaf():  # w przeciwnym wypadku ważniejsze są liście mające znak
            return False
        if self.isLeaf() and other.isLeaf():  # jeżeli jednak oba maja znak, to decyduje kolejność alfabetyczna
            return ord(self.symbol[0]) < ord(other.symbol[0])
        return True

# funkcja służąca do wyświetlenia kodów Huffmana
# na podstawie utworzonego drzewa Huffmana
# oraz obliczenia długości kodu
cnt = 0
def printNodes(node,F,val=''):
    global cnt
    # Kod Huffmana dla bieżącego węzła
    newVal = val + str(node.huff)

    # jeżeli dany węzeł nie jest liściem w drzewie
    # to wywołujemy rekurencję dla lewego i prawego poddrzewa
    if node.left:
        printNodes(node.left, F, newVal)
        printNodes(node.right, F, newVal)

    # jeżeli węzeł jest liściem to wypisujemy kod dla jego znaku
    # i dodajemy ilość znaków do wynikowej długości kodu
    if node.isLeaf():
        # wstawiam kod w odpowiednie miejsce do tablicy F ,aby później wypisywanie było w kolejności
        # odpowiadającej znakom w tablicy S
        F[node.idx] = newVal

        # aktualizuje długość napisu
        cnt += len(newVal) * node.freq

def huffman( S, F ):
    #tworze obiekt kolejki priorytetowej
    nodes = PriorityQueue()

    # tworze liście drzewa, bazując na znakach
    # ilości wystąpień oraz indeksie w tablicy S, a następnei dodajmy do kolejki
    for i in range(len(S)):
        N = node(F[i], S[i], i)
        nodes.put(N)

    # tworze zmienna przechowujaca docelowo korzen drzewa
    rootNode = None
    while nodes.qsize() > 1:  # następnie iteruje, dopóki w nodes nie zostanie ostatni element - korzeń drzewa
        left = nodes.get()    # pobieramy pierwszy, najmniejszy element z PriorityQueue
        right = nodes.get()   # pobieramy kolejny, najmniejszy element z PriorityQueue
        left.huff = '0'       # przypisuje lewemu węzłowi wartość 0
        right.huff = '1'      # przypisuje prawemu węzłowi wartość 1

        # jeżeli oba liście mają tą samą wartość, a jeden z nich jest kontenerem, to powinien on być traktowany jako większy element
        if left.freq == right.freq and not left.isLeaf():
            # dlatego w takiej sytuacji podmieniam wskaźniki
            pom = left
            left = right
            right = pom

        parent = node(left.freq + right.freq,"")  # tworze liść-kontener, który będzie przechowywać dwa powyższe elementy i sumę ich wartości
        rootNode = parent  # ustawiam go na aktualny korzen
        parent.left = left  # i dodaje mu dzieci
        parent.right = right
        nodes.put(parent)

    # Teraz mozna wypisac kody Huffmana i policzyc długość kodu
    printNodes(rootNode,F)
    for i in range(len(S)):
        print(f"{S[i]} : {F[i]}")
    print("dlugosc napisu:",cnt)

S = ["a", "b", "c" ,"d", "e", "f" ]
F = [10 , 11 , 7 , 13, 1 , 20 ]
huffman( S, F)
