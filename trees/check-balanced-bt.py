# Better algorithm here, for poor one scroll down more
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# This code runs in O(N) time and O(H) space, where H is the height of the tree.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root_node):
            # Base case:
            # This is because at the end when child is None, 
            # height is -1, not zero as that's not the child node, 
            # it's just child node's left node which is None
            if not root_node:
                return -1

            leftHeight = getHeight(root_node.left)
            if leftHeight == -sys.maxsize:
                return -sys.maxsize
            
            rightHeight = getHeight(root_node.right)
            if rightHeight == -sys.maxsize:
                return -sys.maxsize
            
            height_diff = leftHeight - rightHeight
            
            if abs(height_diff) > 1:
              return -sys.maxsize
            else:
              return max(leftHeight, rightHeight) + 1
            
        
        return getHeight(root) != -sys.maxsize

# Although this works. it's not very efficient. On each node. we recurse through its entire subtree. This means
# that getHeight is called repeatedly on the same nodes. The algorithm isO(N log N) since each node is
# "touched" once per node above it.
# LogN is for getHeights() and N is for isBalanced() call for every node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root_node):
            # Base case:
            # This is because at the end when child is None, 
            # height is -1, not zero as that's not the child node, 
            # it's just child node's left node which is None
            if not root_node:
                return -1
            return max(getHeight(root_node.left), getHeight(root_node.right) )+ 1
        
        if root is None:
            return True
            
        height_diff = getHeight(root.left) - getHeight(root.right)
                       
        if abs(height_diff) > 1:
          return False
        else:
          return self.isBalanced(root.left) and self.isBalanced(root.right)