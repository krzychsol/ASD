# Krzysztof Solecki
"""
Opis algorytmu: Na początku tworzę kopiec minimum wielkości k+1. Pierwsze k+1 elementów listy wrzucam do kopca.
Iterujac po kolejnych elementach listy odsyłaczowej za każdym razem wyciągam z kopca najmniejszy element i przywracam
własności kopca.Na końcu opróżniam kopiec wyciągając z niego za każdym razem najmniejszy element.
Dla k = 1 wykonuje się algorytm BubbleSort dla list odsyłaczowych, ponieważ jest on wydajniejszy w tym przypdaku od
algroytmu z użyciem kopca. Algorytm jest poprawny, ponieważ za każdym razem pozbywa się najmniejszego elementu oddalonego 
o maksymalnie k pozycji od docelowej i dopina do wynikowej listy.

Złożoność czasowa: O(nlogk) - gdzie n to wielkość listy ,a k to współczynnik chaotyczności listy, w szczególności:
    1)Dla k = O(1) : WYKONUJE BUBBLESORT co daje złożoność O(nk) ,czyli asymptotycznie O(n)
    2)Dla k = O(logn) : asymptotycznie O(nlog(logk))
    3)Dla k = O(n): asymptotycznie O(nlogn)
"""

from .zad1testy import Node, runtests


class Node:
    def __init__(self,val=None):
        self.next = None
        self.val = val


def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return max((i - 1) // 2, 0)


def heapify(H, n, i):
    l = left(i)
    r = right(i)
    largest = i

    if l < n and H[l].val < H[largest].val:
        largest = l
    if r < n and H[r].val < H[largest].val:
        largest = r

    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        heapify(H, n, largest)


def bubblesort(head):
    if head:
        while 1:
            swap = 0
            tmp = head
            while tmp.next:
                if tmp.val > tmp.next.val:
                    swap = 1
                    p = tmp.val
                    tmp.val = tmp.next.val
                    tmp.next.val = p
                    tmp = tmp.next
                else:
                    tmp = tmp.next

            if swap == 0:
                break
            else:
                continue

        return head
    else:
        return head


def insert_to_Q(Q,n,p):
    i = n-1
    Q[i] = p

    while Q[parent(i)].val > Q[i].val:
        Q[parent(i)].val, Q[i].val = Q[i].val, Q[parent(i)].val
        i = parent(i)


def SortH(p, k):
    if k == 0:
        return p

    elif k == 1:
        return bubblesort(p)

    elif k > 1:
        curr = p
        n = 0
        while curr:
            n += 1
            curr = curr.next

        k = min(n - 1, k)

    Q = [Node(float("inf")) for _ in range(k+1)]
    for i in range(k + 1):
        insert_to_Q(Q,i+1,p)
        p = p.next

    newNode = Node()
    result = newNode

    while p is not None:
        Q[0], Q[k] = Q[k], Q[0]
        heapify(Q, k, 0)
        newNode.next = Q[k]
        newNode = newNode.next
        insert_to_Q(Q,k+1,p)
        p = p.next

    for i in range(k, -1, -1):
        Q[0], Q[i] = Q[i], Q[0]
        heapify(Q, i, 0)
        newNode.next = Q[i]
        newNode = newNode.next

    newNode.next = None
    return result.next


runtests(SortH)
