class Node:
    def __init__(self):
        self.next = None
        self.val = None

def merge_reku(L1,L2):
    head = Node()
    if L1 is None:
        return L2
    if L2 is None:
        return L1

    if L1.val <= L2.val:
        head = L1
        head.next = merge_reku(L1.next,L2)
    else:
        head = L2
        head.next = merge_reku(L1,L2.next)

    return head


def merge_iter(L1,L2):
    new = Node()
    res = new

    while L1 is not None and L2 is not None:
        if L1.val <= L2.val:
            new.next = L1
            L1 = L1.next
        else:
            new.next = L2
            L2 = L2.next
        new = new.next

        if L1 is None:
            new.next = L2
        else:
            new.next = L1

    return res.next

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

T1 = [1,1,3,4,7]
T2 = [2,3,6,8]
L1 = tab2list(T1)
L2 = tab2list(T2)

printlist(merge_iter(L1,L2))