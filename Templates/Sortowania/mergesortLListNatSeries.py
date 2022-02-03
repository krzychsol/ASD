#LINKED LIST SECTION-------------------------------------------------

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

#MERGE SORT SECTION----------------------------------------------------------

def merge(L1,L2):
    if L1 == None:
        return L2

    if L2 == None:
        return L1

    if L1.val < L2.val:
        result = L1
        result.next = merge(L1.next,L2)
    else:
        result = L2
        result.next = merge(L1,L2.next)

    return result

def split(L):
    if L is None:
        return L

    while L.next and L.next.val >= L.val:
        L = L.next

    H = L.next
    L.next = None
    return H

def mergesort(L):
    while True:
        NH = None
        NT = None
        while True:
            if L == None:
                L = NH
                break
        A = L
        L,T = split(L)

        if NT == None and L == None:
            return A

        if L == None:
            NT.next = A
            L =NH
            break

        B = L
        L,_ = split(L)
        X,T = merge(A,B)
        if NH == None:
            NH = X
        else:
            NT.next = X
        NT = T

#DRIVER CODE--------------------------------------------------------------------------

T = [1,5,2,4,1,7,3,2,11,2,3]
L = tab2list(T)
mergesort(L)
print(L)





