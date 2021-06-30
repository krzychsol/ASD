class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def tab2list(A):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next

def printlist(L):
    while L != None:
        print(L.val, "->", end=" ")
        L = L.next
    print("|")

def fixsortedlist(L):
    head = L
    curr = L.next
    prev = L
    while curr != None:
        if curr.val < prev.val:
            tmp = curr
            prev.next = curr.next
            tmp.next = L
            L = tmp
            break
        curr = curr.next
        prev = prev.next

    if L.val < L.next.val:
        return L

    tmp = L
    nhead = L.next
    while nhead != None:
        if nhead.val < tmp.val and nhead.next.val > tmp.val:
            tmp2 = nhead.next
            nhead.next = tmp
            tmp.next = tmp2
            break
        nhead = nhead.next

    return head

T = [1,3,4,5,7,8,9,10,11,6]
L = tab2list(T)
printlist(L)
printlist(fixsortedlist(L))