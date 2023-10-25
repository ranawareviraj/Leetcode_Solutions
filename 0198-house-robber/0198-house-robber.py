class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        prev_two = nums[0]
        prev_one = max(nums[0], nums[1])
        result = prev_one

        for house in range(2, n):
            result = max(prev_two + nums[house], prev_one)
            prev_two = prev_one
            prev_one = result
        
        return result
        
        return prev_one
