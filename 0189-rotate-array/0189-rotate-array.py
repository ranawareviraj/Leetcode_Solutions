class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_arr_elements(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        n = len(nums)
        k = k % n # If k is greater than n, effectively we need to copy only n % k elements
        
        reverse_arr_elements(nums, 0, n - 1)
        reverse_arr_elements(nums, 0, k - 1)
        reverse_arr_elements(nums, k, n - 1)
