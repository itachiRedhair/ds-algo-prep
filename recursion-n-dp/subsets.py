 class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            dp = [[] for i in range(len(nums))]
            dp[0].append([])
            dp[0].append([nums[0]])
            for i in range(1, len(nums)):  
                for subset in dp[i-1]: 
                    dp[i].append(subset + [nums[i]])  # with the i'th element
                    dp[i].append(subset)  # without the i'th element
            return dp[len(nums)-1]