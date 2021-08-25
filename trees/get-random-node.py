import random


class TreeNode:
    def __init__(self, val):
        self.size = 1
        self.left = None
        self.right = None
        self.val = val

    def insertInOrder(self, d):
        if d < self.val:
            if not self.left:
                self.left = TreeNode(d)
            else:
                self.left.insertInOrder(d)
        else:
            if not self.right:
                self.right = TreeNode(d)
            else:
                self.right.insertInOrder(d)
        self.size += 1

    def getRandomNode(self):
        randomIndex = random.randint(1, self.size)
        leftSize = self.left.size if self.left else 0
        if randomIndex == self.size:
            return self
        elif randomIndex < leftSize:
            return self.left.getRandomNode()
        else:
            return self.right.getRandomNode()


root = TreeNode(0)
root.insertInOrder(1)
root.insertInOrder(2)
root.insertInOrder(6)
root.insertInOrder(7)
root.insertInOrder(9)
root.insertInOrder(2)
root.insertInOrder(5)
root.insertInOrder(4)
print(root.getRandomNode().val if root else -1)
