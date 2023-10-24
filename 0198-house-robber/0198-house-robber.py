from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @cache # Cache wrapper for memoizing results
        def dp(i):
            # Base Cases: No of houses are 1 or 2 (i = 0, or i = 1)
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            # Find max value based on money we collect,
            # if we rob the current house or not house
            return max(dp(i - 2) + nums[i], dp(i - 1)) 
        
        return dp(len(nums) - 1)