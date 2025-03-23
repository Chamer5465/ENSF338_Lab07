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
    if pivot == None:
        print('Case #1: Pivot not detected.')
    elif (pivot.balance == 1 and data < pivot.data) or (pivot.balance == -1 and data > pivot.data):
        print('Case #2: A pivot exists, and a node was added to the shorter subtree.')
    else:
        print('Case #3 not supported.')
    while parent is not None:
        current = parent
        parent = current.parent
        current.height = 1 + max(getHeight(current.left), getHeight(current.right))
        current.balance = getHeight(current.right) - getHeight(current.left)
        

def non_avl_insert(data, root=None):
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
        
        current = parent
        parent = current.parent
    
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
    theList = [5, 3, 8, 2, 7, 11]
    root = Node(theList[0])
    for e in theList[1:]:
        non_avl_insert(e, root)
    insert(10, root)
    insert(4, root)
    insert(9, root)
    theList = [10, 6, 16, 4, 14, 22]
    root = Node(theList[0])
    for e in theList[1:]:
        non_avl_insert(e, root)
    insert(20, root)
    insert(8, root)
    insert(18, root)
    theList = [15, 9, 24, 6, 21, 33]
    root = Node(theList[0])
    for e in theList[1:]:
        non_avl_insert(e, root)
    insert(30, root)
    insert(12, root)
    insert(27, root)
    theList = [35, 21, 56, 14, 49, 77]
    root = Node(theList[0])
    for e in theList[1:]:
        non_avl_insert(e, root)
    insert(70, root)
    insert(28, root)
    insert(75, root)
    

if __name__ == '__main__':
    main()