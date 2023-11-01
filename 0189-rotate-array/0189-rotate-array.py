class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        end_list = [0] * k
        for i in range(k):
            end_list[k - i - 1] = nums[n - 1 - i]
                
        j = 0
        for i in range(n - 1 - k, -1, -1):
            nums[n - 1 - j] = nums[i]
            j += 1

        for i in range(k):
            nums[i] = end_list[i]
