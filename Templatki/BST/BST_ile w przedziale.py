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


cnt = 0
def countInt(root,a,b):
    global cnt
    curr = root
    if curr is not None:
        countInt(curr.left,a,b)
        if a <= curr.key and curr.key <= b:
            cnt+=1
        if curr.key >= b:
            return
        countInt(curr.right,a,b)


root = BSTNode(10)
insert(root,15)
insert(root,5)
insert(root,8)
insert(root,20)
insert(root,30)
insert(root,2)
insert(root,12)

countInt(root,1,10)
print(cnt)