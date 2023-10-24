class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums, i, memo):
            # If the value cached, return it
            if i in memo:
                return memo[i]

            # Base Cases: No of houses are 1 or 2 (i = 0, or i = 1)
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            # Find max value based on money we collect,
            # if we rob the current house or not house
            memo[i] = max(dp(nums, i - 2, memo) + nums[i], dp(nums, i - 1, memo))
            return memo[i]
        
        memo = {}
        return dp(nums, len(nums) - 1, memo)