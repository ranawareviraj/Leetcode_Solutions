class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = 0
        ans = 0
        for i in range(k):
            curr_sum += arr[i]
        
        ans += (curr_sum / k) >= threshold

        for i in range(k, len(arr)):
            curr_sum += arr[i]
            curr_sum -= arr[i - k]

            ans += (curr_sum / k) >= threshold
        
        return ans
        