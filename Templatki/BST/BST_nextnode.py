class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

def insert(root,key):
    x = root
    last = None
    #przechodze w dół po drzewie do węzła, który będzie rodzicem nowego elementu
    while x is not None:
        last = x
        if key < x.key:
            x = x.left
        elif key > x.key:
            x = x.right
        else:
            #jezeli juz istnieje taka wartosc to przerywamy
            return False

    new = BSTNode(key)
    if key < last.key: #jezeli nowa wartosc jest mniejsza od wartosci rodzica to bedzie to lewy potomek
        last.left = new
        last.left.parent = last
        return True
    else: #jezeli nowa wartosc jest mniejsza od wartosci rodzica to bedzie to prawy potomek
        last.right = new
        last.right.parent = last
        return True

#funkcja pomocnicza znajdujaca zastepczy węzeł podczas usuwania
def getminkey(curr):
    while curr.left:
        curr = curr.left
    return curr

def remove(root,key):
    curr = root

    #przesuwamy sie w dół drzewa az do wartosci ktora zamierzamy usunac
    while curr is not None and curr.key is not key:
        if key < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    #jezeli nie dotarlismy do tej wartosci to znaczy ze nie ma jej w drzewie
    #wówczas przerywamy
    if curr is None or curr.key != key:
        return False

    #Przypadek 1 - usuwamy liść
    if curr.left is None and curr.right is None:
        if curr is not root:
            if curr.parent.left == curr:
                curr.parent.left = None
            else:
                curr.parent.right = None

        return True

    #Przypadek 2 - node ktory usuwamy ma dwojke dzieci
    elif curr.left and curr.right:
        #znajdujemy zastepczy node ktory przepniemy za ten, który usuwamy
        rep = getminkey(curr.right)

        #odłączamy zastepczy node od drzewa
        if rep.parent.left is rep:
            rep.parent.left = None
        else:
            rep.parent.right = None

        #podmieniam zastepczy node za ten ktory ma zostac usuniety
        if curr.parent and curr.parent.left is curr:
            curr.parent.left = rep
        elif curr.parent and curr.parent.right is curr:
            curr.parent.right = rep
        else:
            curr.key = rep.key
        rep.left = curr.left
        rep.right = curr.right
        return True

    #Przypadek 3 - node ktory usuwamy ma jedno dziecko
    else:
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        if curr is not root:
            if curr == curr.parent.left:
                curr.parent.left = child
            else:
                curr.parent.right = child

        return True

def in_order_no_recursion(self):
    stack = []
    elements = []
    current = self
    while current or stack:
        if current:
            stack.append(current)
            current = current.left
        else:
            current = stack.pop()
            elements.append(current.key)
            current = current.right
    return elements

def next_node(p):
    if p.right:
        p = getminkey(p)
    else:
        while p.parent is not None and p.parent.right == p:
            p = p.parent
        if p.parent is not None and p.parent.left == p:
            p = p.parent
        else:
            p = None
    return p

