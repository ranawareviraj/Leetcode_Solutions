class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        product = 1

        for i, num in enumerate(nums):
            result[i] = product
            product *= num
        print(result)
        
        product = 1
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * product
            product *= nums[i]
        
        return result