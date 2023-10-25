class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dp(i, memo):
            # If result in cache, return cached result - Memoization
            if i in memo:
                return memo[i]

            # Base case: When i = 0, below for loop wont be excuted 
            # As it excutes for j if j is less than i that is if its less than 0
            ans = 1

            # ecursively find 
            for j in range(i):
                if nums[j] < nums[i]:
                    # If number at j is less than number at i,
                    # so we have length = len(j) + 1(for ith number)
                    ans = max(ans, dp(j, memo) + 1)
            
            # Add result to cache - Memoization
            memo[i] = ans       
            return ans
        
        max_length = 1
        n = len(nums)
        memo = {}

        # For each index of an array,
        # Find out max_length of increasing subsequence ending at current index
        for i in range(n):
            max_length = max(max_length, dp(i, memo))
        
        return max_length