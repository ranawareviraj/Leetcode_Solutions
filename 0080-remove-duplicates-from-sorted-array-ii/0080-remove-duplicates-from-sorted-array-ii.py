class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        n = len(nums)
        counter = 1

        for right in range(1, n):
            if nums[right] == nums[right - 1]:
                counter += 1
            else:
                counter = 1

            if counter <= 2:
                nums[left] = nums[right]
                left += 1

        return left
