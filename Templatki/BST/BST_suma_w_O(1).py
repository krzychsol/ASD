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

def next_node(p):
    if p.right:
        p = p.right
        p = getminkey(p)
    else:
        while p.parent is not None and p.parent.right == p:
            p = p.parent
        if p.parent is not None and p.parent.left == p:
            p = p.parent
        else:
            p = None
    return p

def sumofBST(root):
    sum = 0
    p = getminkey(root)
    sum += p.key
    while next_node(p) is not None:
        p = next_node(p)
        sum += p.key
    return sum

root = BSTNode(10)
insert(root,5)
insert(root,15)
insert(root,12)
insert(root,13)
insert(root,2)
insert(root,3)
print(sumofBST(root))