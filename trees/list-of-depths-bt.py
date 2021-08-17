# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []
        
        def preOrder(node, level, level_order_list):
            if not node:
                return
            if level != len(level_order_list)-1:
                level_order_list.append([node.val])
            else:
                level_order_list[level].append(node.val)
            preOrder(node.left, level+1, level_order_list)
            preOrder(node.right, level+1, level_order_list)
                
        preOrder(root, 0, level_order_list)
        return level_order_list