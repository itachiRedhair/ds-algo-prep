from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        tracer_arr = list()

        def inorder_traversal(_root):
            if not _root:
                return None
            inorder_traversal(_root.left)
            tracer_arr.append(_root.val)
            inorder_traversal(_root.right)

        inorder_traversal(root)

        print(tracer_arr)

        for i in range(1, len(tracer_arr)):
            if tracer_arr[i] <= tracer_arr[i-1]:
                return False

        return True


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(Solution().isValidBST(root))
