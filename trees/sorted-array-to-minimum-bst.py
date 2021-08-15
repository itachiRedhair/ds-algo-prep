# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        if(len(nums) == 0):
            return None
        mid = int(len(nums)/2)

        middleNode = TreeNode(val=nums[mid])

        middleNode.left = self.sortedArrayToBST(nums[0:mid])
        middleNode.right = self.sortedArrayToBST(nums[mid+1:])

        return middleNode


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).val)
print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).left.val)
print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).left.left.val)
print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).right.val)
print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).right.left.val)
