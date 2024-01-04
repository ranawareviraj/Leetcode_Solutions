class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counter = Counter()
        result = []
        n = len(nums)

        for row in nums:
            for num in row:
                counter[num] += 1

        for num, freq in counter.items():
            if freq == n:
                result.append(num)
        
        return result