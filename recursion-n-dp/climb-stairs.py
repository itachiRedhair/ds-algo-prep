class Solution:
    def climbStairs(self, n: int) -> int:
        def climbStairsRecurse(n, memo_list):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if memo_list[n]==0:
                memo_list[n] = climbStairsRecurse(n-1, memo_list) + climbStairsRecurse(n-2, memo_list)
            return memo_list[n]
        
        return climbStairsRecurse(n, [0]*(n+1))