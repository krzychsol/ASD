from random import randint

#MERGESORT KLASYCZNY [ O(nlogn) ] - wersja 1.0 do poprawy
#CO POPRAWIĆ : UWZGLĘDNIĆ SERIE NATURALNE !!!

#LINKED LIST SECTION  ----------------------------------------------------------------------

class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

def tab2list( A ):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node(A[i])
        C.next = X
        C = X
    return H.next

def printList( h ):
    if h == None:
        return h
    while h:
        print(h.val,end="->")
        h = h.next

#MERGESORT SECTION-----------------------------------------------------------------------

def merge(L1, L2):
    head = Node()

    if L1 is None:
        return L2

    if L2 is None:
        return L1

    if L1.val <= L2.val:
        head = L1
        head.next = merge(L1.next,L2)
    else:
        head = L2
        head.next = merge(L1,L2.next)

    return head

def cutlist(L):
    slow = L
    fast = L

    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next

    mid = slow.next
    slow.next = None
    return L,mid

def mergesort(L):
    if L == None or L.next == None:
        return L

    L1,L2 = cutlist(L)
    L1 = mergesort(L)
    L2 = mergesort(L2)
    L = merge(L1,L2)
    return L

#DRIVER CODE SECTION-------------------------------------------------------------------

T1 = [1,7,4,5,3,5,8,6]
L1 = tab2list(T1)
printList(mergesort(L1))


