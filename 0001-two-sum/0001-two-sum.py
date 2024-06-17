class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, x in enumerate(nums):
            complement = target - x

            for j in range(i + 1, len(nums)):
                if nums[j] == complement:
                    return [i, j]

        return [-1, -1]
