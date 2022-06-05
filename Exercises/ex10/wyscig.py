# Król Bitocji postanowił zorganizować serię wyścigów samochodowych. Wyścigi mają się odbywać po trasach
# zamkniętych, składających się z odcinków autostrady łączących miasta Bitocji. Król chce, żeby każde
# miasto było zaangażowane w dokładnie jeden wyścig. W tym celu należy sprawdzić, czy da się wynająć
# odpowiednie odcinki autostrad. Należy jednak pamiętać o następujących ograniczeniach:
#   1) w Bitocji wszystkie autostrady są jednokierunkowe,
#   2) z każdego miasta wychodzą co najwyżej dwa odcinki autostrady, którymi można dojechać do innych
# miast,
#   3) do każdego miasta dochodzą co najwyżej dwa odcinki autostrady, którymi można przyjechać z innych
# miast.
# Proszę zaproponować algorytm, który mając na wejściu opis sieci autostrad Bitocji sprawdza czy da się
# zorganizować serię wyścigów tak, żeby przez każde miasto przebiegała trasa dokładnie jednego.

"""
Opis dzialania:

Preprocessing: Tworzymy tablice przechowujaca ilosc krawedzi wchodzacych do kazdego wierzcholka
oraz tablice przechowujaca informacje czy wchodza 2 krawedzie i czy wychodza 2 krawedzie
Nastepnie usuwamy zbedne krawedzie w grafie:

Jeśli dany wierzcholek ma 2 krawedzie wychodzace i 2 wchodzace i jedna z nich wchodzi do wierzcholka
ktory ma 2 krawedzie wchodzace to mozna ją usunac.
Nastepnie sprawdzam na kazdego wierzcholka czy jest w jakims cyklu,
jesli nie to sprawdzam czy posiada podwojna krawedz.
Na koncu sprawdzam czy wszystkie wierzcholki sa odwiedzone
"""


def detect_cycle(G, source):
    n = len(G)
    visited = [False] * n
    parent = [None] * n
    return dfs(G, source, visited, parent)


def dfs(G, source, visited, parent):
    visited[source] = True
    for v in G[source]:
        if not visited[v]:
            parent[v] = source
            return dfs(G, v, visited, parent)
        elif visited[v] and parent[source] != v:
            return True, visited
    return False, None


def double_edge(G, source):
    n = len(G)
    visited = [False] * n
    for u in G[source]:
        if source in G[u]:
            visited[source] = True
            visited[u] = True
            return True, visited
    return False, None


def racing(G):
    n = len(G)
    in_out = [[] for _ in range(n)]
    in_count = [0] * n

    # dla kazdego wierzcholka licze krawedzie wchodzace
    for i in range(n):
        for j in range(len(G[i])):
            in_count[G[i][j]] += 1

    # dla kazdego wierzcholka sprawdzam czy posiada 2 wchodzace i 2 wychodzace
    for i in range(n):
        if in_count[i] == 2:
            in_out[i].append(0)
        if len(G[i]) == 2:
            in_out[i].append(1)

    # jezeli ktorys wierzcholek nie ma krawedzi wchodzacych lub
    # nie ma dwoch wchodzacych lub dwoch wychodzacych
    # to nie da sie zorganizowac wyscigu
    for i in range(n):
        if in_count[i] == 0 or len(in_out[i]) == 0:
            return False

    # usuwam nadmiarowe krawedzie
    to_remove = []
    for i in range(n):
        if len(in_out[i]) > 1:
            for j in G[i]:
                if 0 in in_out[j]:
                    to_remove.append((i, j))
                    in_out[i].remove(1)
                    in_out[j].remove(0)
    for i in range(len(to_remove)):
        G[to_remove[i][0]].remove(to_remove[i][1])

    # sprawdzam cykle
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            result, visit = detect_cycle(G, i)
            if not result:
                result, visit = double_edge(G, i)
                if not result:
                    return False
                else:
                    for i in range(len(visit)):
                        if visit[i]:
                            visited[i] = True
            else:
                for i in range(len(visit)):
                    if visit[i]:
                        visited[i] = True

    for i in range(len(visited)):
        if not visited[i]:
            return False
    return True


G = [[1, 2],
     [2, 3],
     [0, 4],
     [4],
     [3]]
print(racing(G))
