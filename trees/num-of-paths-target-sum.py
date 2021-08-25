# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countPaths(_root, _targetSum, _runningSum, _pathCountHashMap):
            if not _root:
                return 0
            _runningSum += _root.val
            _sum = _runningSum - _targetSum
            totalPaths = _pathCountHashMap[_sum] if _sum in _pathCountHashMap else 0
            
            if _runningSum == _targetSum:
                totalPaths += 1
                
            if _runningSum in _pathCountHashMap:
                _pathCountHashMap[_runningSum] = _pathCountHashMap[_runningSum] + 1
            else:
                _pathCountHashMap[_runningSum] = 1
            
            totalPaths += countPaths(_root.left, _targetSum, _runningSum, _pathCountHashMap)
            totalPaths += countPaths(_root.right, _targetSum, _runningSum, _pathCountHashMap)
            if _runningSum in _pathCountHashMap:
                _pathCountHashMap[_runningSum] = _pathCountHashMap[_runningSum] - 1
            elif _pathCountHashMap[_runningSum] == 1:
                del _pathCountHashMap[_runningSum]
                
            return totalPaths
            
        return countPaths(root, targetSum, 0, {})