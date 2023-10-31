class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 1:
            return n
        
        left = 0
        for right in range(0, n):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1

