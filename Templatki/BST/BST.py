class BSTNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
        self.parent = None

def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)

def insert(root, key):
    curr = root
    parent = None

    if root is None:
        return BSTNode(key)

    while curr:
        parent = curr

        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right

    if key < parent.data:
        parent.left = BSTNode(key)
    else:
        parent.right = BSTNode(key)

    return root


if __name__ == '__main__':

    keys = [15, 10, 20, 8, 12, 16, 25,10]

    root = None
    for key in keys:
        root = insert(root, key)

    inorder(root)