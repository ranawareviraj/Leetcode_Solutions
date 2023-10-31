class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        counter = 0

        for right in range(n):
            if nums[left] == nums[right]:
                counter += 1
                if counter == 2:
                    left += 1
                    nums[left] = nums[right]
            else:
                left += 1
                nums[left] = nums[right]
                counter = 1

        return left + 1
            