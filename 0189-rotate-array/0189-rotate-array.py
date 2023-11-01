class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n # If k is greater than n, effectively we need to copy only n % k elements
        
        # Get last k elements from the list
        end_list = [0] * k
        for i in range(k):
            end_list[k - i - 1] = nums[n - 1 - i]

        # Move remaining elements by k positions(to the end of the list)
        pivot = n - 1 - k
        for i in range( pivot, -1, -1 ):
            nums[i + k] = nums[i]

        # Lastly, copy last k elements at the start of the list
        for i in range(k):
            nums[i] = end_list[i]
