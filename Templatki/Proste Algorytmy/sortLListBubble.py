class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def bubble(head):
    sorted = False
    while sorted == False:
        first = head
        sorted = True

    while first.next != None:
        if first.val > first.next.val:
            value = first.val
            first.val = first.next.val
            first.next.val = value
            sorted = False
        first = first.next

    return head

T = [2,4,5,2,6,1]
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

L = tab2list(T)
printlist(bubble(L))
