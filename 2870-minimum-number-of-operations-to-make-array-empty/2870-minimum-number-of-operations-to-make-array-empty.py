class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        
        for freq in counter.values():
            if freq == 1: 
                return -1
            ans += freq // 3 + int(freq % 3 != 0)
        
        return ans