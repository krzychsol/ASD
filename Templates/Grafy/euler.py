from copy import deepcopy
from collections import deque
'''
Algorytm w funkcji euler kopiuje oryginalną macierz i działa na kopii, aby nie nieszczyć oryginalego grafu.
Nastepnie oblicza stopnie wierzchołków w grafie - jeśli któryś z nich jest nieparzysty to nie istnieje cykl eulera i przerywamy algorytm.
Jeśli jednak stopnie wierzchołków są parzyste to znajdujemy cykl. W tym celu uruchamiamy DFS dla pierwszego wierzchołka i przy każdym przetworzeniu wierzchołka
dodajemy go na początek wynikowej kolejki ( w trakcie przetwarzania usuwamy krawedzie przez które już przeszliśmy ).

Złożoność algorytmu: Czasowa: O(V*E) ,czyli O(n^3)
                     Pamięciowa: O(V^2) ,czyli O(n^2)
'''

def euler(G):
    n = len(G)
    G_cpy = G.copy() #kopiuje oryginalna macierz
    numofadj = []
    for i in range(n):
        numofadj.append(sum(G_cpy[i])) #zapisuje do tablicy stopien kazdego z wiechołków
        if numofadj[i] % 2 == 1 or numofadj[i] == 0: #jezeli jakiś wierzchołek ma stopien nieparzysty lub graf jest niespojny to nie da sie utowrzyc cyklu Eulera
            return None

    '''lasts = [0] * n  # tablica pozwalajaca zredukowac ilosc iteracji petli
    path = deque()
    cnt = 0
    def DFS(v):
        nonlocal cnt
        while lasts[v] < n:
            cnt += 1
            if G_cpy[v][lasts[v]] == 1:
                G_cpy[v][lasts[v]] = 0
                G_cpy[lasts[v]][v] = 0
                lasts[v] += 1
                DFS(lasts[v]-1)
            else:
                lasts[v] += 1
        path.appendleft(v)

    DFS(0)'''
    stack = [] #stos do przechowywania przetwarzanych wierzcholkow
    path = [] #wynikowy cykl
    lasts = [0]*n #tablica pozwalajaca zredukowac ilosc iteracji petli
    cur = 0 #poczatkowy wierzcholek
    stack_len = 0
    cnt = 0
    while stack_len > 0 or numofadj[cur] != 0:
        cnt += 1
        if numofadj[cur] == 0: #przetworzylismy wierzcholek
            path.append(cur) #dodajemy go to poczatku cyklu
            cur = stack.pop() #teraz biezacy wierzcholek jest tym ktory jest jest ostatnim z przetwarzanych wczesniej
            stack_len -= 1
        else:
            while lasts[cur] < n: #zaczynamy od wierzcholka na kotrym ostatnio skonczylismy
                cnt += 1
                if G_cpy[cur][lasts[cur]] == 1: #jezeli istnieje krawedz nieodwiedzona
                    stack.append(cur) #to dodajemy wierzcholek do stosu
                    stack_len += 1

                    G_cpy[cur][lasts[cur]] = 0 #usuwamy krawedzie miedzy tymi wierzcholkami
                    G_cpy[lasts[cur]][cur] = 0

                    numofadj[lasts[cur]] -= 1 #zmnijeszamy stopien tych wierzcholków o 1
                    numofadj[cur] -= 1
                    lasts[cur] += 1

                    cur = lasts[cur]-1 #wykonujemy petle dla nowego wierzcholka
                    break
                else:
                    lasts[cur] += 1
    print(cnt)
    return path

### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[0, 1, 1, 0, 0, 0],
     [1, 0, 1, 1, 0, 1],
     [1, 1, 0, 0, 1, 1],
     [0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 1],
     [0, 1, 1, 1, 1, 0]]

H = [[1 for _ in range(45)]for _ in range(45)]
for i in range(len(H)):
    H[i][i] = 0

print(euler(H))

GG = deepcopy(G)
cycle = euler(G)

if cycle == None:
    print("Błąd (1)!")
    exit(0)

u = cycle[0]
for v in cycle[1:]:
    if GG[u][v] == False:
        print("Błąd (2)!")
        exit(0)
    GG[u][v] = False
    GG[v][u] = False
    u = v

for i in range(len(GG)):
    for j in range(len(GG)):
        if GG[i][j] == True:
            print("Błąd (3)!")
            exit(0)

print("OK")



