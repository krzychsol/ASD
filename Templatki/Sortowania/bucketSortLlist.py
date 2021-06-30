class Node():
    def __init__(self):
        self.val = None
        self.next = None

def gettail(head):
    while head != None and head.next != None:
        head = head.next
    return head


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

def bucketsort(head):
    cur = head
    n = 0
    maxval = cur.val
    minval = cur.val
    while cur != None:
        if maxval < cur.val:
            maxval = cur.val
        if minval > cur.val:
            minval = cur.val
        n += 1
        cur = cur.next

    norm = maxval-minval
    buckets = [None for i in range(n)]
    while head != None:
        head_next = head.next
        norm_val = (head.val-minval)/norm
        index = int(n*norm_val)
        if index != n:
            head.next = buckets[index]
            buckets[index] = head
        else:
            head.next = buckets[index-1]
            buckets[index-1] = head
        head = head_next

    for i in range(n):
        buckets[i] = insertionSort(buckets[i])

    first = None
    i = 0
    while i < n:
        if buckets[i] != None:
            if first == None:
                first = buckets[i]
            tail = gettail(buckets[i])
            j = i + 1
            while j < n and buckets[j] == None:
                j += 1
            if j < n:
                tail.next = buckets[j]
            else:
                return first
            i = j
        else:
            i += 1

    return first

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

if __name__ == '__main__':
    T =[18,12,67,34,22,55,32,1,43,29]
    L = tab2list(T)
    printlist(bucketsort(L))