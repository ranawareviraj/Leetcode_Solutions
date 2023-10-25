class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n

        # Base Cases: No of houses are 1 or 2 (i = 0, or i = 1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            # Find max value based on money we collect,
            # if we rob the current house or not house
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp[n - 1]