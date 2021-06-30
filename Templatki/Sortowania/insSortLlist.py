class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

def insSort(head):
    h = head
    if h == None:
        return None
    if h.next == None:
        return h

    i = h.next
    while i :
        key = i.val
        j = i.prev
        while j != None and j.val > key:
             j.next.val = j.val
             j = j.prev
        j.next.val = key
        i = i.next
    return h

