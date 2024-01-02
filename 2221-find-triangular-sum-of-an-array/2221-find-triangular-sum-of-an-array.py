class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        curr = [num for num in nums]
        n = len(nums)
        
        while n > 1:
            arr_sum = [0] * (n - 1)
            for i in range(n - 1):
                arr_sum[i] = (curr[i] + curr[i + 1]) % 10
            
            n -= 1
            curr = arr_sum

        return curr[0] % 10