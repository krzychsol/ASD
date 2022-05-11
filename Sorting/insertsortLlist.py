class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def insertionSort(L):
    sorted = None

    curr = L
    while curr != None:
        next = curr.next
        sorted = sortedInsert(sorted, curr)
        curr = next

    L = sorted
    return L

def sortedInsert(L, new_node):
    if L == None or L.val >= new_node.val:
        new_node.next = L
        L = new_node
    else:
        curr = L
        while curr.next != None and curr.next.val < new_node.val:
            curr = curr.next

        new_node.next = curr.next
        curr.next = new_node

    return L

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

T =[5,4,3,2,1]
L = tab2list(T)
printlist(insertionSort(L))