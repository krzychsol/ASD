'''
Algorytm wykorzystuje drzewo BST w taki sposob ze najpierw wstawia do niego pierwszy klocek z listy.
Nastpenie dla kazdego kolejnego wykonujemy sprawdzenie czy jego przedzial zawiera sie w korzeniu jesli tak to idziemy w prawo i sprawdzamy dalej,
przy czym jednosczesnie poszerzamy w biezacym węźle przedział o ten ktory powstanie w wyniku położenia na nim nowego klocka. Wstawienie klocka na prawo od rodzica oznacza
,że dołożyliśmy klocek do naszej wieży i stała się wyższa wiec aktualizujemy w tym momencie wysokosc w dodawanym nodzie. Jeżeli wstawimy klocek na lewo to oznacza ze wysokosc wiezy sie nie
powiekszyła. Na koniec szukamy maksymalnej wysokosci w utowrzonym drzewie BST.

Złożoność algorytmu to O(n*h) ,gdzie n - to ilosc klockow , h to wysokosc drzewa
'''

class BSTNode:
    def __init__(self, a,b,h):
        self.brick = (a,b,h)
        self.left = None
        self.right = None
        self.parent = None

def includes(A,B): #czy przedzial B zawiera sie w A
    if A[0] >= B[1]:
        return False
    if A[1] <= B[0]:
        return False
    return True

def insert(root,brick):
    x = root
    last = None
    while x is not None:
        last = x
        if includes(x.brick,brick): #jezeli nowy klocek zawiera sie w przedziale to dodajemy go do wieży
            x.brick = (min(x.brick[0],brick[0]),max(x.brick[1],brick[1]),x.brick[2]) #aktualizujemy zakres i wysokosc wiezy
            x = x.right #idziemy w prawo
        else: #jezeli przedzial sie nie zawiera to idziemy w lewo
            x = x.left

    new = BSTNode(brick[0],brick[1],brick[2]) #tworze nowy node (klocek)
    if includes(last.brick,brick): #jezeli zawiera sie w ostatnim sprawdzanym klocku to dodajemy na szczyt
        last.right = new
        new.brick = (brick[0],brick[1],last.brick[2]+brick[2])
        new.parent = last
    else: #jezeli sie nie zawiera to stawiamy na poziomie na kotrym byl jego rodzic ( o ile istnieje )
        last.left = new
        new.parent = last
        tmp = new
        flag = False
        while tmp.parent:
            if tmp.parent.right == tmp:
                tmp = tmp.parent
                flag = True
                break
            tmp = tmp.parent

        if flag:
            new.brick = (new.brick[0],new.brick[1],tmp.brick[2]+brick[2]) #poprawic

def getminkey(curr):
    while curr.left:
        curr = curr.left
    return curr

def next_node(p):
    if p.right:
        p = p.right
        p = getminkey(p)
    else:
        while p.parent is not None and p.parent.right == p:
            p = p.parent
        if p.parent is not None and p.parent.left == p:
            p = p.parent
        else:
            p = None
    return p

def block_height( K ):
    T = BSTNode(K[0][0],K[0][1],K[0][2])
    n = len(K)
    for i in range(1,n):
        insert(T,K[i])

    p = getminkey(T)
    h = p.brick[2]
    while next_node(p) is not None:
        p = next_node(p)
        h = max(h,p.brick[2])
    return h

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

K1 = [ (1,3,1), (2,5,2), (0,3,2), (8,9,3), (4,6,1) ]
R1 = 5

K2 = [(1,3,1), (2,4,1), (3,5,1), (4,6,1), (5,7,1), (6,8,1)]
R2 = 6

K3 = [(1,10**10,1)]
R3 = 1

TESTY = [(K1,R1),(K2,R2),(K3,R3)]

good = True
for KK, RR in TESTY:
  print("Klocki           : ", KK )
  print("Oczekiwany wynik : ", RR )
  WW = block_height( KK )
  print("Otrzymany wynik  : ", WW )
  if WW != RR:
     print("Błąd!!!!")
     good = False
     
if good: print("OK!")
else   : print("Problemy!")