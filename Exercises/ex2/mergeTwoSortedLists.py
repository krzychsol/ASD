class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


# wersja rekurencyjna
def merge_lists_reku(l1,l2):
    head = Node()
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val <= l2.val:
        head = l1
        head.next = merge_lists_reku(l1.next,l2)
    else:
        head = l2
        head.next = merge_lists_reku(l1,l2.next)

    return head

# wersja iteracyjna
def merge_lists(l1, l2):
    if l1 is None and l2 is None:
        return None
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    merged = Node()
    head = merged
    while l1 is not None or l2 is not None:
        if l1 is None:
            merged.next = l2
            l2 = l2.next
        elif l2 is None:
            merged.next = l1
            l1 = l1.next
        elif l1.val <= l2.val:
            merged.next = l1
            l1 = l1.next
        else:
            merged.next = l2
            l2 = l2.next
        merged = merged.next

    return head.next


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


T1 = [1, 2, 3, 4, 5]
T2 = [0, 3, 3, 3, 6, 7]
L1 = tab2list(T1)
L2 = tab2list(T2)
printlist(merge_lists_reku(L1,L2))
