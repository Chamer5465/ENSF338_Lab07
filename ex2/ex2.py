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


    def getHeight(self):
        leftHeight = 0
        rightHeight = 0
        if self.left != None:
            leftHeight = self.left.getHeight()
        if self.right != None:
            rightHeight = self.right.getHeight()
        if self.right != None or self.left != None:
            self.height = max(leftHeight, rightHeight) + 1
        return self.height
        
    def getBalance(self):
        if self.right == None and self.left == None:
            return 0
        elif self.left == None:
            self.balance = self.right.getHeight()
        elif self.right == None:
            self.balance = - self.left.getHeight()
        else:
            self.balance = self.right.getHeight() - self.left.getHeight()
        return self.balance

def insert(data, root=None):
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
        parent.getHeight()
    else:
        parent.right = Node(data, parent)
        parent.getHeight()

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

def inOrderBalance(root):
    stack = []
    current = root
    maxBalance = 0

    while current is not None or len(stack) > 0:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        if (abs(current.getBalance()) > maxBalance):
            maxBalance = abs(current.getBalance())
        current = current.right

    return maxBalance



def main():
    theList = [x for x in range(1000)]
    timeList = []
    absoluteBalance = []
    for x in range(1000):
        random.shuffle(theList)
        root = Node(theList[0])
        for i in theList[1:]:
            insert(i, root)
        totalTime = 0
        for i in range(1000):
            totalTime += timeit.timeit(lambda: search(i, root), number=1)
        absoluteBalance.append(inOrderBalance(root))
        timeList.append(totalTime / 1000)
    plt.figure(figsize=(10, 20))
    plt.scatter(absoluteBalance, timeList)
    plt.xlabel('Max Absolute Balance')
    plt.ylabel('Average Time to Search')
    plt.title('Average Performance vs Max Absolute Balance')
    plt.show()

    


        


if __name__ == '__main__':
    main()