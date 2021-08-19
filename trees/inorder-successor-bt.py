class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Solution:
    def find_inorder_successor(self, node):
        if not node:
            return None

        def leftmost_node(_node):
            if not _node:
                return None
            while _node.left:
                _node = _node.left
            return _node

        if node.right:
            return leftmost_node(node.right)
        else:
            while node.parent and node.parent.right is node:
                node = node.parent
        return node.parent


root = TreeNode(1)
root.left = TreeNode(2)
root.left.parent = root
root.left.left = TreeNode(4)
root.left.left.parent = root.left
root.right = TreeNode(3)
root.right.parent = root
root.right.left = TreeNode(5)
root.right.left.parent = root.right
root.right.left.left = TreeNode(7)
root.right.left.left.parent = root.right.left
root.right.left.right = TreeNode(8)
root.right.left.right.parent = root.right.left
root.right.right = TreeNode(6)
root.right.right.parent = root.right

input_node =root.right.left.left

print(Solution().find_inorder_successor(input_node).val)
