class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i, memo):
            # Return cached result - Memoization
            if i in memo:
                return memo[i]

            ans = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    ans = max(ans, dp(j, memo) + 1)
            
            # Add result to cache - Memoization
            memo[i] = ans       
            return ans
        
        max_length = 1
        n = len(nums)
        memo = {}
        for i in range(n):
            max_length = max(max_length, dp(i, memo))
        
        return max_length