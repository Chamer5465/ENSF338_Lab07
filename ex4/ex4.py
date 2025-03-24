class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1
        self.balance = 0

def leftRotate(pivot):
    new_root = pivot.right  # identify the root

    pivot.right = new_root.left  # update the subtree connections
    if new_root.left:  # if there is one. this will become the RIGHT subtree of pivot
        new_root.left.parent = pivot
        
    # link the pivot to the new root
    new_root.left = pivot
    new_root.parent = pivot.parent
    if pivot.parent:
        if pivot.parent.left == pivot:
            pivot.parent.left = new_root
        else:
            pivot.parent.right = new_root
    pivot.parent = new_root
    
    # update the height and balance
    pivot.height = 1 + max(getHeight(pivot.left), getHeight(pivot.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    
    pivot.balance = getHeight(pivot.right) - getHeight(pivot.left)
    new_root.balance = getHeight(new_root.right) - getHeight(new_root.left)
    
    return new_root

def rightRotate(pivot):
    new_root = pivot.left  # identify the root

    pivot.left = new_root.right
    if new_root.right:  # if there is one. this will become the LEFT subtree of pivot
        new_root.right.parent = pivot
        
    # link the pivot to the new root
    new_root.right = pivot
    new_root.parent = pivot.parent
    if pivot.parent:
        if pivot.parent.left == pivot:
            pivot.parent.left = new_root
        else:
            pivot.parent.right = new_root
    pivot.parent = new_root
    
    # update the height and balance
    pivot.height = 1 + max(getHeight(pivot.left), getHeight(pivot.right))
    new_root.height = 1 + max(getHeight(new_root.left), getHeight(new_root.right))
    
    pivot.balance = getHeight(pivot.right) - getHeight(pivot.left)
    new_root.balance = getHeight(new_root.right) - getHeight(new_root.left)
    
    return new_root

def _lr_rotate(pivot):
    print('LR rotate')
    pivot.left = leftRotate(pivot.left)
    return rightRotate(pivot)

def _rl_rotate(pivot):
    print('RL rotate')
    pivot.right = rightRotate(pivot.right)
    return leftRotate(pivot)

def insert(data, root=None):
    current = root
    parent = None
    pivot = None
    while current is not None:
        parent = current
        if current.balance != 0:
            pivot = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)
    
    if pivot is None:
        print('Case #1: Pivot not detected.')
    elif (pivot.balance == 1 and data < pivot.data) or (pivot.balance == -1 and data > pivot.data):
        print('Case #2: A pivot exists, and a node was added to the shorter subtree.')
    else:
        if (pivot.balance == 1 and data > pivot.data and data > pivot.right.data) or (pivot.balance == -1 and data < pivot.data and data < pivot.left.data):
            print('Case #3a: adding a node to an outside subtree')
            if pivot.balance == -1:
                root = rightRotate(pivot)
            else:
                root = leftRotate(pivot)
        else:
            print('Case #3b: adding a node to an inside subtree')
            if pivot.balance == -1:
                root = _lr_rotate(pivot)
            else:
                root = _rl_rotate(pivot)

    while parent is not None:
        current = parent
        parent = current.parent
        current.height = 1 + max(getHeight(current.left), getHeight(current.right))
        current.balance = getHeight(current.right) - getHeight(current.left)
    
    return root

def getHeight(root):
    if root is None:
        return 0
    return root.height


def main():
    print("\n--- Testing Case 3a (Outside subtree) ---")
    root = Node(10)
    root = insert(5, root)
    root = insert(15, root)
    root = insert(25, root)  
    root = insert(30, root)
    
    print("\n--- Testing Case 3b (LR rotation: Inside subtree) ---")
    root = Node(10)
    root = insert(5, root)
    root = insert(7, root)
    
    print("\n--- Testing Case 3b (RL rotation: Inside subtree) ---")
    root = Node(10)
    root = insert(15, root)
    root = insert(14, root)


    
if __name__ == '__main__':
    main()


