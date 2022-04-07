class Node:
    def __init__(self):
        self.next = None
        self.val = None

def cut(head):
    while head.next and head.next.val > head.val:
        head = head.next
    res = head.next
    head.next = None
    return res

def mergeNatSeries(L):
    if L is None:
        return None

    next_head = cut(L)

    if next_head is None:
        return L


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