import random
import timeit
from matplotlib import pyplot as plt

class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
        self.height = 1
        self.balance = 0
        
def non_AVL_insert(data, root=None):
    current = root
    parent = None
    while current is not None:
        parent = current
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
    
    while parent != None:
        parent.height = 1 + max(getHeight(parent.left), getHeight(parent.right))
        
        parent.balance = getHeight(parent.right) - getHeight(parent.left)
        
        if (parent.balance == 1 and data < parent.data) or (parent.balance == -1 and data > parent.data):
            print('Case #2: A pivot exists, and a node was added to the shorter subtree.')
            current = parent
            parent = current.parent
            continue
        elif (parent.balance != 0):
            print('#Case #3 not supported.')
            current = parent
            parent = current.parent
            continue
        
        current = parent
        parent = current.parent
        
        print('Case #1: Pivot not detected.')
        

def insert(data, root=None):
    if root == None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(data, root.left)
    elif data > root.data:
        root.right = insert(data, root.right)
        
    root.height = 1 + max(getHeight(root.right), getHeight(root.left))
    
    root.balance = getHeight(root.right) - getHeight(root.left)
    
    if (root.balance == 1 and data < root.data) or (root.balance == -1 and data > root.data):
        print('Case #2: A pivot exists, and a node was added to the shorter subtree.')
        return root
    elif (root.balance != 0):
        print('#Case #3 not supported.')
        return root
    
    print('Case #1: Pivot not detected.')
    return root
        
    
def getHeight(root):
    if root == None:
        return 0
    return root.height
    
        
    
    
def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None



def main():
    theList = [x for x in range(10)]
    random.shuffle(theList)
    root = Node(theList[0])
    for e in theList[1:]:
        non_AVL_insert(e, root)
    print('lets go')
    

if __name__ == '__main__':
    main()