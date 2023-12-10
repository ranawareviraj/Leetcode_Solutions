class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeroes_count = 0
        longest_ones = 0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes_count += 1
            
            while zeroes_count > k:
                if nums[left] == 0:
                    zeroes_count -= 1
                left += 1
            
            longest_ones = max(longest_ones, right - left + 1)
        
        return longest_ones
            