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

def kthSmallest(root, i, k):
    if root is None:
        return float("inf"), i

    left, i = kthSmallest(root.left, i, k)

    if left != float("inf"):
        return left, i

    i = i + 1

    if i == k:
        return root.key, i

    return kthSmallest(root.right, i, k)

def findKthSmallest(root, k):
    i = 0
    return kthSmallest(root, i, k)[0]


keys = [10, 20, 8, 12, 16, 25]

root = BSTNode(15)
for key in keys:
    insert(root, key)

k = 2
result = findKthSmallest(root, k)

if result != float("inf"):
    print(result)
