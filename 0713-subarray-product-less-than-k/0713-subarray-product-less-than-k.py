class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if (k <= 1): return 0
        n = len(nums)
        product = 1
        left = 0
        number_of_subarrays = 0

        for right in range(n):
            product *= nums[right]

            while product >= k:
                product /= nums[left]
                left += 1
            
            number_of_subarrays += (right - left + 1)

        return number_of_subarrays
