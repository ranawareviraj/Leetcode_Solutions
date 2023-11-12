class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        minimum = -math.inf

        for num in nums:
            if num - minimum > k:
                ans += 1
                minimum = num
        
        return ans
