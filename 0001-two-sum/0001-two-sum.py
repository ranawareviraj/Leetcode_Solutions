class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = defaultdict(int)

        for i, x in enumerate(nums):
            complement = target - x
            if complement in seen:
                return [i, seen[complement]]

            seen[x] = i

        return [-1, -1]
