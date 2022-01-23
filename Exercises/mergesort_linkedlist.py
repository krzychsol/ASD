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

def printList(head):
    if head is None:
        return head
    while head:
        print(head.val,end=" -> ")
        head = head.next

def merge(L1,L2):
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

    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        slow = slow.next

    mid = slow.next
    slow.next = None
    return L,mid

def mergesort(L):
    if L is None or L.next is None:
        return L

    L1,L2 = cutlist(L)
    L1 = mergesort(L1)
    L2 = mergesort(L2)
    L = merge(L1,L2)
    return L

A = [5,3,4,1,2,8,9,14,2,3]
L = tab2list(A)
printList(mergesort(L))