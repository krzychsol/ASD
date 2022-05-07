from Exams.Exam2k21.Termin0.zad2testy import runtests

class Node:
    def __init__(self):
        self.left = None
        self.leftval = 0
        self.right = None
        self.rightval = 0
        self.X = None


def valuableTree(T:Node,k):
    size = k
    T.X = [[None for _ in range(k+1)] for __ in range(k+1)]

    # Największe poddrzewo pod T nie licząc T
    def g(T, k):
        nonlocal size
        if T.X is None:
            T.X = [[None for _ in range(size + 1)] for __ in range(size + 1)]

        if k > 0 and T.left is None and T.right is None:
            return -float("inf")

        if k == 0:
            T.X[1][k] = 0
            return 0

        if T.X[1][k]:
            return T.X[1][k]

        # sa obie krawedzie
        if T.left and T.right:
            if T.X[1][k]:
                T.X[1][k] = max(T.X[1][k], g(T.left, k), g(T.right, k), f(T.left, k), f(T.right, k))
            else:
                T.X[1][k] = max(g(T.left, k), g(T.right, k), f(T.left, k), f(T.right, k))

        # jest lewa tylko
        if T.left:
            if T.X[1][k]:
                T.X[1][k] = max(T.X[1][k], g(T.left, k), f(T.left, k))
            else:
                T.X[1][k] = max(g(T.left, k), f(T.left, k))

        # jest tylko prawa
        if T.right:
            if T.X[1][k]:
                T.X[1][k] = max(T.X[1][k], g(T.right, k), f(T.right, k))
            else:
                T.X[1][k] = max(g(T.right, k), f(T.right, k))

        return T.X[1][k]

    # Największe poddrzewo pod T włącznie z T
    def f(T: Node, k):
        nonlocal size
        if T.X is None:
            T.X = [[None for _ in range(size + 1)] for __ in range(size + 1)]

        if k > 0 and T.left is None and T.right is None:
            return -float("inf")

        if k == 0:
            T.X[0][k] = 0
            return 0

        if T.X[0][k]:
            return T.X[0][k]

        # biore obie krawedzie
        if T.left and T.right:
            for i in range(k - 1):
                if T.X[0][k]:
                    T.X[0][k] = max(T.X[0][k], T.leftval + T.rightval + f(T.left, k - 2 - i) + f(T.right, i))
                else:
                    T.X[0][k] = T.leftval + T.rightval + f(T.left, k - 2 - i) + f(T.right, i)

        # biore lewa krawedz
        if T.left:
            if T.X[0][k]:
                T.X[0][k] = max(T.X[0][k], T.leftval + f(T.left, k - 1))
            else:
                T.X[0][k] = T.leftval + f(T.left, k - 1)

        # biore prawa krawedz
        if T.right:
            if T.X[0][k]:
                T.X[0][k] = max(T.X[0][k], T.rightval + f(T.right, k - 1))
            else:
                T.X[0][k] = T.rightval + f(T.right, k - 1)

        return T.X[0][k]

    return max(f(T,k),g(T,k))

runtests(valuableTree)



