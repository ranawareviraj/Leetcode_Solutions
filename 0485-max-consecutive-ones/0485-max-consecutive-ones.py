class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        hasZeros = 0
        ans = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                hasZeros = 1
            
            while hasZeros:
                if nums[left] == 0:
                    hasZeros = 0
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans 