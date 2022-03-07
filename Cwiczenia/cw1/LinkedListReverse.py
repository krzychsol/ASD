class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def list_reverse(head):
    back = head
    first = head.next
    back.next = None

    while first:
        next = first.next
        first.next = back
        back = first
        first = next

    return back


# do wyswietlania i testow
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


T = [1, 2, 3, 4, 5]
L = tab2list(T)
printlist(list_reverse(L))
