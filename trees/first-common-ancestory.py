# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def covers(_root, _node):
            if not _root:
                return False
            if _root is _node:
                return True
            return covers(_root.left, _node) or covers(_root.right, _node)

        def findLCA(_root, _p, _q):
            p_on_left = covers(_root.left, _p)
            q_on_left = covers(_root.left, _q)

            if(p_on_left != q_on_left):
                return _root

            return findLCA(_root.left, p, q) if p_on_left else findLCA(_root.right, p, q)

        if not covers(root, p) or not covers(root, q):
            return None

        if covers(p, q):
            return p
        if covers(q, p):
            return q

        return findLCA(root, p, q)


root = TreeNode(3)
root.left = TreeNode(5)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left
q = root.left.right.right

print(Solution().lowestCommonAncestor(root, p, q).val)
