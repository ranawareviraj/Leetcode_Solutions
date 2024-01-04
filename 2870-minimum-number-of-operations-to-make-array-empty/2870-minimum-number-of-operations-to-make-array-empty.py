class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        
        for key in counter:
            freq = counter[key]
            if freq == 1: 
                return -1
            ans += ceil(freq / 3)
        
        return ans