"""
Pewna kraina składa się z wysp pomiędzy którymi istnieją połączenia lotnicze, promowe oraz mosty.
Pomiędzy dwoma wyspami istnieje co najwyżej jeden rodzaj połączenia. Koszt przelotu z wyspy
na wyspę wynosi 8B, koszt przeprawy promowej wynosi 5B, za przejście mostem trzeba wnieść
opłatę 1B. Poszukujemy trasy z wyspy A na wyspę B, która na kolejnych wyspach zmienia środek
transportu na inny oraz minimalizuje koszt podróży.
Dana jest tablica G, określająca koszt połączeń pomiędzy wyspami. Wartość 0 w macierzy
oznacza brak bezpośredniego połączenia. Proszę zaimplementować funkcję islands( G, A, B )
zwracającą minimalny koszt podróży z wyspy A na wyspę B. Jeżeli trasa spełniająca warunki zadania
nie istnieje, funkcja powinna zwrócić wartość None
"""

"""
Moje rozwiązanie : Klasyczna Dijkstra dla grafu w reprezentacji macierzowej ,z tą różnicą ,że w tablicy
z dystansami do danych wierzchołków trzymam nie tylko najkrótszy dystans do danego wierzchołka ,ale też środek
transportu jakim się do niego dostaliśmy i przy relaksacji krawędzi grafu sprawdzam czy nie powtarzam 
drugi raz tego samego środka transportu

Złożoność czasowa taka jak dla Dijkstry macierzowej ,czyli : O(n^2)
"""

def minDistance(G,dist,visited):
    global min_idx
    min = float("inf")
    n = len(G)
    for v in range(n):
        if dist[v][0] < min and visited[v] == False:
            min = dist[v][0]
            min_idx = v
    return min_idx

def islands(G,A,B):
    n = len(G)
    dist = [[float("inf"),0] for _ in range(n)]
    dist[A] = (0,0)
    visited = [False for _ in range(n)]

    for _ in range(n):
        u = minDistance(G,dist,visited)
        visited[u] = True
        for v in range(n):
            if G[u][v] > 0 and visited[v] == False and dist[v][0] > dist[u][0]+G[u][v] \
                    and (G[u][v] != dist[u][1] or dist[u][1] == 0):
                dist[v][0] = dist[u][0]+G[u][v]
                dist[v][1] = G[u][v]

    if dist[B][0] == float("inf"):
        return None
    return dist[B][0]

G1 = [[0, 5, 1, 8, 0, 0, 0],
    [5, 0, 0, 1, 0, 8, 0],
    [1, 0, 0, 8, 0, 0, 8],
    [8, 1, 8, 0, 5, 0, 1],
    [0, 0, 0, 5, 0, 1, 0],
    [0, 8, 0, 0, 1, 0, 5],
    [0, 0, 8, 1, 0, 5, 0]]

G2 = [[0,1,8,0,0,0,0],
      [1,0,5,0,0,0,0],
      [8,5,0,1,0,0,0],
      [0,0,1,0,1,0,0],
      [0,0,0,1,0,5,8],
      [0,0,0,0,5,0,1],
      [0,0,0,0,8,1,0]]

print(islands(G2,0,6))