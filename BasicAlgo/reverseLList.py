class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(l): #odwrocenie listy
    f = l.first
    if f == None:
        return f

    p = None
    q = f
    while q != None:
        r = q.next
        q.next = p
        p = q
        q = r

    return p
