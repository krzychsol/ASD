from EGZAMIN20.Termin3.zad3testy import runtests
import heapq
from collections import deque

class Node:
    def __init__( self, val ):
        self.next = None
        self.val = val

def tab2list(T):
    if len(T) == 0:
        return None
    frst = Node(T[0])
    tmp = frst
    for i in range(1,len(T)):
        e2 = Node(T[i])
        tmp.next = e2
        tmp = tmp.next
    return frst

def printlist(h):
    while h is not None:
        print(h.val,end=" ")
        h = h.next

def merge(T):
    k = len(T)
    n = 0
    for i in range(k):
        for j in range(len(T[i])):
            n += 1

    first_elems = []
    for i in range(k):
        if T[i]:
            first_elems.append((T[i][0],i))
    heapq.heapify(first_elems)
    res = []

    while len(res) < n:
        elem,idx = heapq.heappop(first_elems)
        T[idx].pop(0)
        if T[idx]:
            new_elem = T[idx][0]
            heapq.heappush(first_elems,(new_elem,idx))
        res.append(elem)

    L = tab2list(res)
    return L

T = [[0,1,2,4,5],[0,10,20],[5,15,25]]
runtests( merge )
