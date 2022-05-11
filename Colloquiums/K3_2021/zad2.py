from zad2testy import runtests
from math import inf

class BNode:
    def __init__( self, value ):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


def cutthetree(T):
    if T is None:
        return 0
    if T.right is None and T.left is None:
        return inf
    actual_value = inf
    if T.parent is not None:
        actual_value = T.value
    actual_value = min(actual_value, cutthetree(T.right) + cutthetree(T.left))
    return actual_value

    
runtests(cutthetree)


