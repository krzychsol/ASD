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

root = BSTNode(10)
insert(root,15)
insert(root,5)
insert(root,8)
insert(root,20)
insert(root,30)
insert(root,2)
insert(root,12)

def prev(root,key):
    curr = root
    while curr is not None and curr.key is not key:
        if key < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    if curr.left:
        curr = curr.left
        while curr.right:
            curr = curr.right
        return curr
    elif curr.parent:
        if curr.parent.right == curr:
            return curr.parent
        if curr.parent.left == curr:
            while curr.parent.right:
                if curr.parent == root:
                    return None
                curr = curr.parent
            return curr.parent

    return None

x = prev(root,20)
print(x.key)

def getminkey(curr):
    while curr.left:
        curr = curr.left
    return curr


def inOrderSuccessor(n):
    if n.right is not None:
        return getminkey(n.right)

    p = n.parent
    while p is not None:
        if n != p.right:
            break
        n = p
        p = p.parent
    return p

def next(root,key):
    curr = root
    while curr is not None and curr.key is not key:
        if key < curr.key:
            curr = curr.left
        else:
            curr = curr.right

    if curr.right:
        return getminkey(curr.right)

    p = curr.parent
    while p != None:
        if curr != p.right:
            break
        curr = p
        p = p.parent
    return p

x = inOrderSuccessor(root.right.left)
print(x.key)