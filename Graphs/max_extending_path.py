from queue import PriorityQueue
from copy import deepcopy

'''
Algorytm działa bardzo podobnie do algorytmu Dijkstry, z tą różnicą ,że relaksacja odbywa się w taki sposób,że maksymalizuje minimalną przebustowość
krawędzi od źródła do bieżącego wierzchołka. W trakcie algorytmu gramadzone są i na bieżąco aktualizowane informacje o "rodzicach" każdego z wierzchołków
w celu późniejszego odtworzenia szukanej ścieżki. Samo szukanie odbywa się rekurencyjnie właśnie w oparciu o juz zebrane informacje o rodzicach.

Złożoność czasowa algorytmu: O(Elog(V)) ,gdzie E oznacza liczbę krawędzi ,a V liczbę wierzchołków w grafie.
Uzasadnienie złożoności: główna część algorytu działa w czasie O(ElogV) ,ponieważ jest to lekko zmodyfikowany algorytm Dijkstry dla grafu w reprezentacji
listy sąsiedztwa. Użycie kolejki priorytetowej powoduje ,że każda opracja na niej jest w czasie O(logV). Dla grafów gęstych taka implementacja ma złożoność
rzędu O(V^2logV) ,natomiast dla grafów rzadkich będzie to O(VlogV).
'''

def max_extending_path(G, s, t):
    n = len(G)
    cap = [-float("inf")] * n #Tablica zawieracjąca maksymalna przepustowosc do kazdego wirzcholka
    parent = [-1] * n #Tablica sluzaca do odtworzenia wyniku
    pq = PriorityQueue() #wierzcholki beda przetwarzane w kolejce priorytetowej
    pq.put((0, s))
    cap[s] = float("inf")
    while not pq.empty():
        tmp = pq.get()
        u = tmp[1] #pobieram z kolejki numer wierzcołka ,do którego wartosc przepustowosci jest najwieksza

        for v in G[u]:
            d = max(cap[v[0]],min(cap[u], v[1])) #obliczam max z bieżącej maksymalnej przepustowosci do wierzcholka v ,oraz z minimum z przepustowosci do u
                                                 #oraz przepustowości na krawędzi {u,v}.
            if d > cap[v[0]]:  #jeśli jest wieksza niz dotychczas to ją aktualizuje
                cap[v[0]] = d
                parent[v[0]] = u
                pq.put((d, v[0]))


    path = []
    def printpath(parent,t): #funkcja rekurenycjna ,odtwarzająca optymalną ścieżkę
        nonlocal path
        if parent[t] == -1:
            path.append(t)
            return
        printpath(parent,parent[t])
        path.append(t)

    printpath(parent,t)
    return path


### sprawdzenie czy dla grafu G (o ktorym zakladamy, ze ma cykl Eulera
### funkcja zwraca prawidłowy wynik

G = [[(1, 4), (2, 3)],  # 0
     [(3, 2)],  # 1
     [(3, 5)],  # 2
     []]  # 3
s = 0
t = 3
C = 3

GG = deepcopy(G)
path = max_extending_path(GG, s, t)

print("Sciezka :", path)

if path == []:
    print("Błąd (1): Spodziewano się ścieżki!")
    exit(0)

if path[0] != s or path[-1] != t:
    print("Błąd (2): Zły początek lub koniec!")
    exit(0)

capacity = float("inf")
u = path[0]

for v in path[1:]:
    connected = False
    for (x, c) in G[u]:
        if x == v:
            capacity = min(capacity, c)
            connected = True
    if not connected:
        print("Błąd (3): Brak krawędzi ", (u, v))
        exit(0)
    u = v

print("Oczekiwana pojemność :", C)
print("Uzyskana pojemność   :", capacity)

if C != capacity:
    print("Błąd (4): Niezgodna pojemność")
else:
    print("OK")

