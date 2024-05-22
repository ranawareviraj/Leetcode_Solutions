class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        map = defaultdict(int)
        for x in nums:
            map[x] += 1
            if map[x] > 2:
                return False

        return True
