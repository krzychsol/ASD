class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def insertToSortedList(head, val):
    if head is None or val < head.val:
        new = Node(val)
        new.next = head
        head = new
    else:
        curr = head
        while curr.next is not None and curr.next.val < val:
            curr = curr.next

        new = Node(val)
        new.next = curr.next
        curr.next = new

    return head


def insertionSortList(head):
    sorted = None
    curr = head

    while curr:
        next = curr.next
        sorted = insertToSortedList(sorted,curr.val)
        curr = next

    head = sorted
    return head

### do wyswietlania i testow 
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


T = [5, 4, 3, 2, 1]
L = tab2list(T)
printlist(insertionSortList(L))
