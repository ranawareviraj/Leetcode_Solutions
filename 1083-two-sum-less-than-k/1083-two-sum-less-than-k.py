class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        seen = set()
        nums.sort()
        left = 0
        right = len(nums) - 1

        result = -1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                result = max(result, curr_sum)
                left += 1
            else:
                right -= 1
        
        return result
        
